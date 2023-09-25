import requests

response  = requests.post('https://test-stand.gb.ru/login', data ={'username: "GB202306042a214"', 'password: "e778a3dca7"'})

print(response.status_code)
print(response)
