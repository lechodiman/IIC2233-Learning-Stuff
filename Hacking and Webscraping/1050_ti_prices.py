import requests
from bs4 import BeautifulSoup


def get_prices(page_number=1):

    base_url = 'http://www.solotodo.com'
    url = 'http://www.solotodo.com/video_cards/?advanced_controls=0&keywords=&ordering=&gpu=546616&min_price=26900&max_price=719900&page_number={}'.format(page_number)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    results = soup.find_all('div', {'class': 'search_result'})
    for result in results:
        gpu_name = result.h4.strong.text
        link = base_url + result.h4.strong.a['href']
        price = result.find('a', {'class': 'search-result-price'}).text

        print('gpu_name: {}'.format(gpu_name))
        print('price: {}'.format(price))
        print('link: {}'.format(link))
        print()


for i in range(1, 3):
    get_prices(i)
