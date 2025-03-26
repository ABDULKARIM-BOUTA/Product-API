import requests

endpoint = 'http://127.0.0.1:8000/api/product/3/update/'
data = {
    'name': 'RX 9700',
    'price': '650'
}
response = requests.put(endpoint, json=data)
print(response.json())