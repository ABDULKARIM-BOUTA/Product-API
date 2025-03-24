import requests

# this client has nothing to do with the api,
# it is way of pf python to interact with django rest framework,
# imitating a web client interacting with api

#endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/'

response = requests.get(endpoint)
print(response.text)
print(response.status_code)