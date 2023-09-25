import requests

S = request.Sesions()

def get_sites(lat, long, radius, limit=100):
  
    URL = "https://en.wikipedia.org/w/api/php"
    params = {
         "format": "json",
         "list": "geosearch",
         "gscoord": f"{lat}|{long}",
         "gslimit": f"{limit}",
         "gsradius": f"{radius}",
         "action": "query"
    }
    r = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    PLACES = DATA['query']['geosearch']
    sites = [i["title"] for i in PLACES]
    for place in PLACES:
      print(place['title'])

