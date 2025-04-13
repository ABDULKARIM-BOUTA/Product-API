import requests

auth_endpoint = 'https://rest-api-dj.up.railway.app/api/auth/'
username = input('Username:')
password = input('Password:')

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = { 'Authorization': f'token {token}'}

    endpoint = 'https://rest-api-dj.up.railway.app/api/product/create/'

    # new record's data
    data = {
        'name': 'Shadow Of The Coluses',
        'price': '45'
    }
    response = requests.post(endpoint, data=data, headers=headers)
    print(response.json())

