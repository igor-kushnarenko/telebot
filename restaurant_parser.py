import requests
from bs4 import BeautifulSoup

HOST = 'https://dovilleresort.ru'
URL = 'https://dovilleresort.ru/restaurant/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-md-4 col-sm-6 col-centered col-restaurant')
    # print(items)
    data = []

    for item in items:
        data.append(
            {
                'title': item.find('img').get('title'),
                'period': item.find('span', class_='detail').get_text(strip=True),
                'desc': item.find('div', class_='caption').get_text(strip=True),
                'href': HOST + item.find('a', class_='btn btn-block btn-offers').get('href'),
            }
        )
    return data


def get_text_restaurant_parser(items):
    acc = []
    for pos in items:
        description = pos['desc'].split(sep='.')
        acc.append(f"{pos['title'].upper()}\n{pos['period']}\n{description[0]}\n{pos['href']}\n")
    return acc


html = get_html(URL)
items = get_content(html.text)
restaurant_obj_text = get_text_restaurant_parser(items)


