import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# print(soup.title)
# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# print(soup.get_text())
# for url in soup.find_all('a'):
#     print(url.get('href'))

nav = soup.nav

# print(nav)
#
# for url in nav.find_all('a'):
#     print(url.get('href'))

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
