import requests
import urllib

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = 'santiago'
url = main_api + urllib.parse.urlencode({'address': address})

json_data = requests.get(url).json()
print(json_data)

json_status = json_data['status']

formatted_address = json_data['results'][0]['formatted_address']

print(json_status)
print()
print(formatted_address)
