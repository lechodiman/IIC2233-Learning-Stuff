from bs4 import BeautifulSoup
import requests
from urllib import parse


class LinkFinder():

    def __init__(self, base_url, page_url):
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def feed(self):
        req = requests.get(self.page_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        for link in soup.find_all('a'):
            url = parse.urljoin(self.base_url, link['href'])
            self.links.add(url)

    def get_page_links(self):
        return self.links


if __name__ == '__main__':
    finder = LinkFinder('https://thenewboston.com', 'https://thenewboston.com/')
    finder.feed()
    print(*finder.get_page_links(), sep='\n')
