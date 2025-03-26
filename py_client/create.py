import requests

endpoint = 'http://127.0.0.1:8000/api/product/create/'
data = {
    'name': 'I7-9700',
    'price': '150'
}
response = requests.post(endpoint, json=data)
print(response.json())