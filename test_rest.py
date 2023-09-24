import requests

S = request.Sesions()

def get_sites(lat, long, radius, limit=100):
  
    URL = "https://en.wikipedia.org/w/api/php"
    params = {
         "format": "json",
         "list": "geosearch",
         "gscoord": "37.7891838|-122.4033522",
         "gslimit": "10",
         "gsradius": "10000",
         "action": "query"
    }
r
