"""Various pieces of data and mapping of stop names to codes."""

places = {'place-alfcl': 'Alewife',
 'place-alsgr': 'Allston Street',
 'place-andrw': 'Andrew',
 'place-aport': 'Airport',
 'place-aqucl': 'Aquarium',
 'place-armnl': 'Arlington',
 'place-asmnl': 'Ashmont',
 'place-astao': 'Assembly',
 'place-babck': 'Babcock Street',
 'place-bbsta': 'Back Bay',
 'place-bckhl': 'Back of the Hill',
 'place-bcnfd': 'Beaconsfield',
 'place-bcnwa': 'Washington Square',
 'place-belsq': 'Bellingham Square',
 'place-bland': 'Blandford Street',
 'place-bmmnl': 'Beachmont',
 'place-bndhl': 'Brandon Hall',
 'place-bomnl': 'Bowdoin',
 'place-boxdt': 'Box District',
 'place-boyls': 'Boylston',
 'place-brdwy': 'Broadway',
 'place-brico': 'Packards Corner',
 'place-brkhl': 'Brookline Hills',
 'place-brmnl': 'Brigham Circle',
 'place-brntn': 'Braintree',
 'place-bucen': 'Boston University Central',
 'place-buest': 'Boston University East',
 'place-butlr': 'Butler',
 'place-buwst': 'Boston University West',
 'place-bvmnl': 'Brookline Village',
 'place-capst': 'Capen Street',
 'place-ccmnl': 'Community College',
 'place-cedgr': 'Cedar Grove',
 'place-cenav': 'Central Avenue',
 'place-chels': 'Chelsea',
 'place-chhil': 'Chestnut Hill',
 'place-chill': 'Chestnut Hill Avenue',
 'place-chmnl': 'Charles/MGH',
 'place-chncl': 'Chinatown',
 'place-chswk': 'Chiswick Road',
 'place-clmnl': 'Cleveland Circle',
 'place-cntsq': 'Central',
 'place-coecl': 'Copley',
 'place-cool': 'Coolidge Corner',
 'place-crtst': 'Courthouse',
 'place-davis': 'Davis',
 'place-denrd': 'Dean Road',
 'place-dwnxg': 'Downtown Crossing',
 'place-eliot': 'Eliot',
 'place-engav': 'Englewood Avenue',
 'place-estav': 'Eastern Avenue',
 'place-fbkst': 'Fairbanks Street',
 'place-fenwd': 'Fenwood Road',
 'place-fenwy': 'Fenway',
 'place-fldcr': 'Fields Corner',
 'place-forhl': 'Forest Hills',
 'place-gover': 'Government Center',
 'place-grigg': 'Griggs Street',
 'place-grnst': 'Green Street',
 'place-haecl': 'Haymarket',
 'place-harsq': 'Harvard',
 'place-harvd': 'Harvard Avenue',
 'place-hsmnl': 'Heath Street',
 'place-hwsst': 'Hawes Street',
 'place-hymnl': 'Hynes Convention Center',
 'place-jaksn': 'Jackson Square',
 'place-jfk': 'JFK/UMass',
 'place-kencl': 'Kenmore',
 'place-knncl': 'Kendall/MIT',
 'place-kntst': 'Kent Street',
 'place-lake': 'Boston College',
 'place-lech': 'Lechmere',
 'place-lngmd': 'Longwood Medical Area',
 'place-longw': 'Longwood',
 'place-masta': 'Massachusetts Avenue',
 'place-matt': 'Mattapan',
 'place-mfa': 'Museum of Fine Arts',
 'place-miltt': 'Milton',
 'place-mispk': 'Mission Park',
 'place-mlmnl': 'Malden Center',
 'place-mvbcl': 'Maverick',
 'place-newtn': 'Newton Highlands',
 'place-newto': 'Newton Centre',
 'place-north': 'North Station',
 'place-nqncy': 'North Quincy',
 'place-nuniv': 'Northeastern University',
 'place-ogmnl': 'Oak Grove',
 'place-orhte': 'Orient Heights',
 'place-pktrm': 'Park Street',
 'place-plsgr': 'Pleasant Street',
 'place-portr': 'Porter',
 'place-prmnl': 'Prudential',
 'place-qamnl': 'Quincy Adams',
 'place-qnctr': 'Quincy Center',
 'place-rbmnl': 'Revere Beach',
 'place-rcmnl': 'Roxbury Crossing',
 'place-river': 'Riverside',
 'place-rsmnl': 'Reservoir',
 'place-rugg': 'Ruggles',
 'place-rvrwy': 'Riverway',
 'place-sbmnl': 'Stony Brook',
 'place-sdmnl': 'Suffolk Downs',
 'place-shmnl': 'Savin Hill',
 'place-smary': 'Saint Marys Street',
 'place-smmnl': 'Shawmut',
 'place-sougr': 'South Street',
 'place-spmnl': 'Science Park',
 'place-sstat': 'South Station',
 'place-state': 'State Street',
 'place-sthld': 'Sutherland Road',
 'place-stplb': 'Saint Paul Street',
 'place-stpul': 'Saint Paul Street',
 'place-sull': 'Sullivan Square',
 'place-sumav': 'Summit Avenue',
 'place-symcl': 'Symphony',
 'place-tapst': 'Tappan Street',
 'place-tumnl': 'Tufts Medical Center',
 'place-valrd': 'Valley Road',
 'place-waban': 'Waban',
 'place-wascm': 'Washington Street',
 'place-welln': 'Wellington',
 'place-wimnl': 'Wood Island',
 'place-wlsta': 'Wollaston',
 'place-wondl': 'Wonderland',
 'place-woodl': 'Woodland',
 'place-wrnst': 'Warren Street',
 'place-wtcst': 'World Trade Center'
}

activityMap = {
    'USING_WHEELCHAIR': "in wheelchair/need step-free access",
    'USING_ESCALATOR': "limited mobility/need escalator",
    "BOARD": "boarding transit",
    "EXIT": "exiting transit",
    "RIDE": "riding transit"
}


greenlineStops = {'Allston Street': 'place-alsgr',
 'Arlington': 'place-armnl',
 'Babcock Street': 'place-babck',
 'Back of the Hill': 'place-bckhl',
 'Beaconsfield': 'place-bcnfd',
 'Blandford Street': 'place-bland',
 'Boston College': 'place-lake',
 'Boston University Central': 'place-bucen',
 'Boston University East': 'place-buest',
 'Boston University West': 'place-buwst',
 'Boylston': 'place-boyls',
 'Brandon Hall': 'place-bndhl',
 'Brigham Circle': 'place-brmnl',
 'Brookline Hills': 'place-brkhl',
 'Brookline Village': 'place-bvmnl',
 'Chestnut Hill': 'place-chhil',
 'Chestnut Hill Avenue': 'place-chill',
 'Chiswick Road': 'place-chswk',
 'Cleveland Circle': 'place-clmnl',
 'Coolidge Corner': 'place-cool',
 'Copley': 'place-coecl',
 'Dean Road': 'place-denrd',
 'Eliot': 'place-eliot',
 'Englewood Avenue': 'place-engav',
 'Fairbanks Street': 'place-fbkst',
 'Fenway': 'place-fenwy',
 'Fenwood Road': 'place-fenwd',
 'Government Center': 'place-gover',
 'Green Street': 'place-grnst',
 'Griggs Street': 'place-grigg',
 'Harvard Avenue': 'place-harvd',
 'Hawes Street': 'place-hwsst',
 'Haymarket': 'place-haecl',
 'Heath Street': 'place-hsmnl',
 'Hynes Convention Center': 'place-hymnl',
 'Kenmore': 'place-kencl',
 'Kent Street': 'place-kntst',
 'Lechmere': 'place-lech',
 'Longwood': 'place-longw',
 'Longwood Medical Area': 'place-lngmd',
 'Mission Park': 'place-mispk',
 'Museum of Fine Arts': 'place-mfa',
 'Newton Centre': 'place-newto',
 'Newton Highlands': 'place-newtn',
 'North Station': 'place-north',
 'Northeastern University': 'place-nuniv',
 'Packards Corner': 'place-brico',
 'Park Street': 'place-pktrm',
 'Pleasant Street': 'place-plsgr',
 'Prudential': 'place-prmnl',
 'Reservoir': 'place-rsmnl',
 'Riverside': 'place-river',
 'Riverway': 'place-rvrwy',
 'Saint Marys Street': 'place-smary',
 'Saint Paul Street': 'place-stpul',
 'Science Park': 'place-spmnl',
 'South Street': 'place-sougr',
 'Summit Avenue': 'place-sumav',
 'Sutherland Road': 'place-sthld',
 'Symphony': 'place-symcl',
 'Tappan Street': 'place-tapst',
 'Waban': 'place-waban',
 'Warren Street': 'place-wrnst',
 'Washington Square': 'place-bcnwa',
 'Washington Street': 'place-wascm',
 'Woodland': 'place-woodl'
}
