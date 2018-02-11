import requests
from bs4 import BeautifulSoup
from download_img import gen_naturals
import urllib.request

naturals = gen_naturals()
url = 'https://uwaterloo.ca/'
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

all_imgs_span = soup.find_all('span', {'class': 'image'})

imgs = soup.find_all('img')

# Printing 'alt' description for every image
print(*[i['alt'] for i in imgs], sep='\n')

# links_src = []
# for img in imgs:
#     full_name = img['src']
#     if full_name[:1] == '/':
#         full_name = '{}{}'.format(url, full_name)
#
#     links_src.append(full_name)
#
# for link in links_src:
#     filename = next(naturals)
#     image_file = open('{}.jpg'.format(filename), 'wb')
#     image_file.write(requests.get(link).content)
#     image_file.close()
#
# print(*links_src, sep='\n')
