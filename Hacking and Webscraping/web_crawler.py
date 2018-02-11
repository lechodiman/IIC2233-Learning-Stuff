import requests
from bs4 import BeautifulSoup


def search_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.thenewboston.com/search.php?type=1&sort=pop&page={}'.format(page)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        for link in soup.find_all('a', {'class': 'user-name'}):
            href = 'https://thenewboston.com/{}'.format(link.get('href'))
            title = link.text
            print(title)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    req = requests.get(item_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # for item_name in soup.find_all('a', {'href': '#profile-friends-tab'}):
    #     followers = item_name.span.text
    #     print(followers)

    href_set = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href.startswith('http'):
            href = 'https://thenewboston.com/{}'.format(link.get('href'))
        href_set.add(href)

    print(*href_set, sep='\n')

if __name__ == '__main__':
    search_spider(1)
