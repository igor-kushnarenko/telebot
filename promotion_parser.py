import requests
from bs4 import BeautifulSoup

HOST = 'https://dovilleresort.ru'
URL = 'https://dovilleresort.ru/promotions/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='action-cards__col')
    data = []
    for item in items:
        data.append(
            {
                'title': item.find('div', class_='action-card__title').get_text(strip=True),
                'desc': item.find('div', class_='action-card__desc').get_text(strip=True),
                'href': HOST + item.find('a', class_='action-card').get('href'),
            }
        )
    return data


def get_text_promothion_parser(items):
    acc = []
    for i in items:
        acc.append(f"{i['title'].upper()}\n{i['desc']} - {i['href']}\n")
    acc_string = '\n'.join(acc)
    return acc_string


html = get_html(URL)
items = get_content(html.text)
promotion_obj_text = get_text_promothion_parser(items)