import requests

endpoint = 'http://127.0.0.1:8000/api/product/list-create/'
data = {
    'name': 'I7-11700',
    'price': '175'
}
response = requests.post(endpoint, json=data)
print(response.json())