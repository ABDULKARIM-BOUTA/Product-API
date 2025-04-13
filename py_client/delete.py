import requests

auth_endpoint = 'https://rest-api-dj.up.railway.app/api/auth/'
username = input('Username:')
password = input('Password:')

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = { 'Authorization': f'token {token}'}

    item_pk = 6        # replace item_pk with the desired item pk
    endpoint = f'https://rest-api-dj.up.railway.app/api/product/{item_pk}/delete/'
    response = requests.delete(endpoint, headers=headers)

    if response.status_code == 204:
        print("Delete successful:", response.status_code)
    else:
        print(f"Delete failed. Status code: {response.status_code}")
        print("Raw response:", response.text)
else:
    print("Authentication failed:", auth_response.json())
