import requests

def login():
  response  = requests.post('https://test-stand.gb.ru/gateway/login', data={'username: "GB2022111948e18"', 'password: "db4297e3bc"'})
  
  print(response.status_code)
  print(response.json()["token"])
