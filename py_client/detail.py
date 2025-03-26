import requests

endpoint = 'http://127.0.0.1:8000/api/product/3/detail/'
response = requests.get(endpoint)
print(response.json())