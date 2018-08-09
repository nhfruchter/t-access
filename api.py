# Warning: this is messy!

import requests
import datetime
import dateutil.parser
from functools import reduce, lru_cache
from itertools import groupby
import data

def greenline(apikey, stop):
    """
    Return processed green line data for a stop.
    """
    # Only green line trips
    filter_route = "Green-B,Green-C,Green-D,Green-E"

    # Include vehicle and trip data
    include = "vehicle,trip"
    
    # API request
    p = {"filter[route]": filter_route, "include": include, "filter[stop]": stop}
    result = requests.get("https://api-v3.mbta.com/predictions", params=p).json()
    
    return processGreenlinePredictions(result)
        
def processGreenlinePredictions(result):
    """Process MBTA API data on predictions for display."""
    def eta(arrival, departure):
        """Take an arrival, departure datetime string and turn into eta.
        
        returns (hours, minutes, seconds, is_departure)
        """
        if not (arrival or departure):
            return (None, None, None, None)
            
        if arrival:
            is_departure = False
            pred = dateutil.parser.parse(arrival)
        else:
            is_departure = True
            pred = dateutil.parser.parse(departure)
        
        now = datetime.datetime.now(datetime.timezone.utc)
        td = pred - now
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return (hours, minutes, seconds, is_departure)
        
        
    def vehicle(vehicleObject):
        """Takes vehicle object and processes."""
        
        def whichAccessible(state):
            """
            Verbal description of which cars are accessible from
            a tuple of (True, False, ...) for a consist.
            """
            # 1 car
            if len(state) == 1:
                if state[0]:
                    return "any"
                else:
                    return "none"
            # 2 cars        
            elif len(state) == 2:
                back, front = state
                if back and not front:
                    return "back"
                elif front and not back:
                    return "front"    
                elif front and back:
                    return "any"    
                else:
                    return "none"    
            # 3 cars        
            elif len(state) == 3:
                answer = ""
                back, middle, front = state
                if back:
                    answer += "back "
                elif middle:
                    answer += "middle "    
                elif front:
                    answer += "front "
                else:
                    answer = "none"    
                if all(state):
                    answer = "any"
                return answer    
            # L O N G B O I
            # 3+ cars aren't run in regular service    
            else:    
                raise ValueError("This vehicle is too long")

        # If there is data on the vehicle then we can process it
        if vehicleObject['data']:
            vid = vehicleObject['data']['id']
            
            # Search included objects from API call for vehicle ID
            vehicle = [v for v in result['included'] if v['type'] == 'vehicle' and v['id'] == vid][0]
            cars = vehicle['attributes']['label'].split('-')[::-1]

            # Magic number: 38xx, 39xx series car numbers are accessible
            accessibility = [int(cid[0:2]) >= 38 for cid in cars]
            
            # Find correct trip from included objects in API call
            trip = [t for t in result['included'] 
                    if t['type'] == 'trip' 
                    and t['relationships']['vehicle']['data'] 
                    and t['relationships']['vehicle']['data']['id'] == vid][0]
            headsign = trip['attributes'].get('headsign') or "No Data"
            
            # Do some abbreviation
            headsign = headsign.replace("Street", "St").replace("Government", "Gov't").replace("Circle", "Cir")

            return {
                "headsign": headsign,
                "cars": list(zip(cars,accessibility)),
                "n": len(cars),
                "nAccessible": len(accessibility),
                "whichAccessible": whichAccessible(accessibility) 
            }

        else:
            return

    output = []
    # Iterate over each prediction
    for prediction in result['data']:

        thisEta = eta(prediction['attributes']['arrival_time'], prediction['attributes']['departure_time'])
        thisVehicle = vehicle(prediction['relationships']['vehicle'])  

        # Only process vehicles with ETAs
        if any(thisEta):
            thisPrediction = { 
                "arrival": prediction['attributes']['arrival_time'],
                "departure": prediction['attributes']['departure_time'],
                "eta": thisEta,
                "direction": prediction['attributes']['direction_id'],
                "route": prediction['relationships']['route']['data']['id'],
                "vehicle": thisVehicle
            }
            output.append(thisPrediction)

    # Sort by inbound/outbound
    presorted = sorted(output, key=lambda a: a['direction'])
    # And group
    return groupby(presorted, lambda a: a['direction'])    
    

def accessibilityAlerts(apikey, filter_activity="USING_WHEELCHAIR,USING_ESCALATOR", filter_stop=""):
    """Get accessibility alerts for wheelchairs and escalators."""
    
    # Do API call
    p = {"filter[activity]": filter_activity}
    result = requests.get("https://api-v3.mbta.com/alerts", params=p)
    result = result.json()
    
    allStations, processed = processAlerts(result['data'])
    output = {
        "n": len(result['data']),
        "allStations": allStations,
        "alerts": processed
    }
    return output
    
def processAlerts(alerts):
    """Process alert data from MBTA API for display."""
    
    output = []
    # Iterate over alerts
    for alert in alerts:
        attrs = alert['attributes']
        
        # Get location ID
        location = [place for place in [e['stop'] for e in attrs['informed_entity']] if 'place-' in place]
        
        # Otherwise "unknown"
        if len(location):
            location = data.places.get(location[0]) or "Unknown"
        else:
            location = "Unknown"    
            
        # Get relevant GTFS Activities
        activities = set(reduce(list.__add__, [e['activities'] for e in attrs['informed_entity']]))
        activities = [data.activityMap.get(a) for a in activities]
        
        # Craft response
        thisAlert= {
            'location': location,
            'active_for': attrs['active_period'],
            'txt_description': attrs['description'],
            'txt_blurb': attrs['header'],
            'txt_active_for': attrs['timeframe'],
            'txt_effect': attrs['service_effect'],
            'activities': activities
        }
        output.append(thisAlert)
        
    # Sort and group by location
    presort = sorted(output, key=lambda a: a['location'])
    allStations = sorted(set([a['location'] for a in presort]))
    return allStations, groupby(presort, lambda a: a['location'])
        
    
        
