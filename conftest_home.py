import pytest
import yaml
import requests

with open('config_home.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username':'User_1_Login', 'password': '6f831d56c2'})
    token = obj_data.json()['token']
    return token

@pytest.fixture()
def posts():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']},data={
        'username':'User_1_Login',
        'password': '6f831d56c2',
        'title': 'newTitle',
        'description': 'Anything',
        'content':'THAT'S OK'})
    return obj_data.json()['description']
