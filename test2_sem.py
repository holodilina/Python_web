import requests

def login():
  response  = requests.post('https://test-stand.gb.ru/gateway/login', data={'username: "GB2022111948e18"', 'password: "db4297e3bc"'})
  
  if response.status_code == 200
      return response.json()["token"]

print(login())
