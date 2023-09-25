import requests

def login():
  response  = requests.post("https://test-stand.gb.ru/gateway/login", data={'username': "User_1_Login"', 'password: "6f831d56c2"})
  print(response.status_code)
  if response.status_code == 200:
      return response.json()["token"]

def get(token):
  print(token)
  response = requests.get("https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}), params={"owner": "NOTME"}}
  print(resource.JSON())

print(get(login()))
