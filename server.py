from flask import Flask, render_template
from api import accessibilityAlerts, greenline
import data

app = Flask(__name__)
KEY = None # Can be "" for testing

if KEY is None:
    raise ValueError("Please insert an MBTA v3 API key in server.py - https://api-v3.mbta.com/")

@app.route("/")
def getAlerts():
    alerts = accessibilityAlerts("")
    return render_template("main.html", alerts=alerts)

@app.route("/green")
def greenlineHome():
    stops = data.greenlineStops
    return render_template("green-main.html", stops=stops)
    
@app.route("/green/<stopID>")
def greenlineStop(stopID):
    name = data.places.get(stopID)
    predictions = greenline(KEY, stopID)
    return render_template("green-stop.html", name=name, data=predictions, stopID=stopID)
    
if __name__ == '__main__':
    app.run(debug=True)
