import requests
import yaml
import pytest

with open('config_home.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
website = 'https://test-stand.gb.ru/api/posts'
username = 'User_1_Login'
password = '6f831d56c2'

def token_auth(token):
    res = requests.get(url=my_dict["url1"], headers={"X-Auth-Token": token}, params={"owner": "NOTME"})
    content_var = [item["content"] for item in res.json()['data']]
    return content_var

def test_step1(login):
    assert '' in token_auth(login)

def test_step2(postP):
    assert 'ANYTHING' in posts

print(token_auth(my_dict['token']))
