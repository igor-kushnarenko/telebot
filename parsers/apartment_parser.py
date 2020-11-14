import requests
from bs4 import BeautifulSoup as bs4
import fake_useragent

HOST = 'https://dovilleresort.ru/'
URL = 'https://dovilleresort.ru/nomera-price/'
user = fake_useragent.FakeUserAgent().random
HEADERS = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'user_agent': user}


def get_html(url):
    r = requests.get(url)
    return r


def get_content(html):
    soup = bs4(html, 'html.parser')
    items = soup.find_all('div', class_='body')
    # todo вот тут остановился