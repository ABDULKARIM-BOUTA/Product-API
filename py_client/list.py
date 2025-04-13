import requests

endpoint = 'https://rest-api-dj.up.railway.app/api/product/list/'
response = requests.get(endpoint)
print(response.json())
