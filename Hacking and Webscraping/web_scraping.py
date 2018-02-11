from bs4 import BeautifulSoup
import requests


url = 'https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'
r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.content, 'lxml')
# print(soup.prettify())

# all tags of a (links)
# for link in soup.find_all('a'):
#     print("<a href='{}'>{}</a> ".format(link.get('href'), link.text))

g_data = soup.find_all('div', {'class': 'info'})
# print(g_data)

for item in g_data:
    try:
        print(item.contents[0].find_all('a', {'class': 'business-name'})[0].text)
        # print(item.contents[1].find_all('p', {'class': 'adr'})[0].text)
        print(item.contents[1].find_all('span', {'class': 'street-address'})[0].text)
        print(item.contents[1].find_all('span', {'itemprop': 'addressLocality'})[0].text)
        print(item.contents[1].find_all('div', {'class': 'phones phone primary'})[0].text)
    except:
        pass
