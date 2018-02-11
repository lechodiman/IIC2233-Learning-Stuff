import requests
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card'

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

item_titles = soup.find_all('a', {'class': 'item-title'})
# print(item_titles[0].text)
containers = soup.find_all('div', {'class': 'item-container'})

for c in containers:
    brand = c.div.div.a.img['title'] if c.div.div.a else 'Null'
    title = c.find_all('a', {'class': 'item-title'})[0].text
    price_current = c.find_all('li', {'class': 'price-current'})[0]
    price = price_current.strong.text + price_current.sup.text
    shipping_price = c.find_all('li', {'class': 'price-ship'})[0].text.strip()
    print('Brand: {}'.format(brand))
    print('Title: {}'.format(title))
    print('Price: {}'.format(price))
    print('Shipping price: {}'.format(shipping_price))
    print()
