import requests

auth_endpoint = 'https://rest-api-dj.up.railway.app/api/auth/'
username = input('Username:')
password = input('Password:')

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {'Authorization': f'token {token}'}

    item_pk = 6        # replace item_pk with the desired item pk
    endpoint = f'https://rest-api-dj.up.railway.app/api/product/{item_pk}/update/'
    data = {
        'price': '70',
    }

    response = requests.patch(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        print("Update successful:", response.json())
    elif response.status_code == 204:
        print("Update successful (no content returned).")
    else:
        print(f"Update failed. Status code: {response.status_code}")
        print("Raw response:", response.text)
else:
    print("Authentication failed:", auth_response.json())