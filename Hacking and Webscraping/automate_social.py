import requests

api_key = '426d78df234396e7'

params = {
    'apiKey': api_key,
    'email': 'lechodiman@uc.cl'
}

url = 'https://api.fullcontact.com/v2/person.json'
req = requests.get(url, params=params)
print(req.json())
