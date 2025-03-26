import requests

endpoint = 'http://127.0.0.1:8000/api/product/3/delete/'
response = requests.delete(endpoint)
print(response.status_code)