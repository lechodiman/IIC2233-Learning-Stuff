import requests

r = requests.get('http://localhost:8080/api/square', params={'v1': '10', 'v2': '2'})
print('cuadrado: {}'.format(r.text))

r = requests.get('http://localhost:8080/api/sum', params={'v1': '10', 'v2': '2'})
print('suma: {}'.format(r.text))
