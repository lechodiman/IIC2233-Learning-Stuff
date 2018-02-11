import requests

r = requests.get('http://localhost:8080')
print('/: {}'.format(r.text))

r = requests.get('http://localhost:8080/recursos')
print('/recursos: {}'.format(r.text))

r = requests.get('http://localhost:8080/recursos/1')
print('/recursos/id: {}'.format(r.text))
