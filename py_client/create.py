import requests

endpoint = 'http://127.0.0.1:8000/api/product/create/'
data = {
    'name': 'RTX 3060',
    'price': '300'
}
response = requests.post(endpoint, json=data)
print(response.json())