import requests

import yaml

with open("config2_sem.yaml") as f:
  data = yaml.safe_load(f)

def login():
  response  = requests.post(data[url_login], data={'username': data["login"], 'password': data[password]})
  print(response.status_code)
  if response.status_code == 200:
      return response.json()["token"]

def get(token):
 
  resource = requests.get(data[url_posts], headers={"X-Auth-Token": token}), params={"owner": "NOTME"}}
  return resource.json()


