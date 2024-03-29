import requests
from bs4 import BeautifulSoup
import fake_useragent

HOST = 'https://dovilleresort.ru'
URL = 'https://dovilleresort.ru/promotions/'
user = fake_useragent.FakeUserAgent().random
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': user
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
    counter = 0
    for i in items:
        counter += 1
        acc.append(f"{i['title'].upper()}\n{i['desc']} - {i['href']}\n")
        if counter >= 3:
            break
    acc_string = '\n'.join(acc)
    return acc_string


html = get_html(URL)
items = get_content(html.text)
promotion_obj_text = get_text_promothion_parser(items)
