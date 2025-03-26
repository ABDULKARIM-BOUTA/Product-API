import requests

# this client has nothing to do with the api,
# it is way of pf python to interact with django rest framework,
# imitating a web client interacting with api

endpoint = 'http://127.0.0.1:8000/api/'

response = requests.post(endpoint, json={'name':'gamepad', 'price':'30'})

print(response.json())