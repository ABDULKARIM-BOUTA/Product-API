import requests

record_ip = 2

endpoint = f'https://rest-api-dj.up.railway.app/api/product/{record_ip}/detail/'
response = requests.get(endpoint)
print(response.json())
