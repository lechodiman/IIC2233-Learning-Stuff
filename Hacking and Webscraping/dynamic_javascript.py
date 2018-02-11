from bs4 import BeautifulSoup
import requests
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebPage, QWebFrame


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()

soup = BeautifulSoup(source, 'lxml')
js_test = soup.find('p', {'class': 'jstest'})
print(js_test.text)
