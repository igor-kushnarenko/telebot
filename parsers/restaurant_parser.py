import fake_useragent
import requests
from bs4 import BeautifulSoup

from rest_period_parser import time_dict


HOST = 'https://dovilleresort.ru'
URL = 'https://dovilleresort.ru/restaurant/'
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
    # print(data)
    return data


def get_text_restaurant_parser(items):
    block_content = [
        'Снек-бар Bon appetit',
        'Снек-бар на пляже Le Paradis',
        'Детское кафе Карамелька',
    ]
    acc = []
    for name, time in time_dict.items():
        for pos in items:
            if pos['title'] not in block_content:
                if pos['title'].upper() == name:
                    description = pos['desc'].split(sep='.')
                    acc.append(f"{pos['title'].upper()}\n{pos['period']}\n{time}\n{description[0]}\n{pos['href']}\n")
    # print(acc)
    acc_string = '\n'.join(acc)
    return acc_string


def get_rest_list(items):
    restraunt_list = [
        'Ресторан Normandie',
        'Гастрономический ресторан Saint Michel',
    ]
    acc = []
    for name, time in time_dict.items():
        for pos in items:
            if pos['title'] in restraunt_list:
                if pos['title'].upper() == name:
                    description = pos['desc'].split(sep='.')
                    acc.append(f"{pos['title'].upper()}\n{pos['period']}\n{time}\n{description[0]}\n{pos['href']}\n")
    acc_string = '\n'.join(acc)
    return acc_string


def get_bar_list(items):
    bar_list = [
        'DISCO BAR',
        'Снек-бар Marinie',
        'Lobby Bar',
    ]
    acc = []
    for name, time in time_dict.items():
        for pos in items:
            if pos['title'] in bar_list:
                if pos['title'].upper() == name:
                    description = pos['desc'].split(sep='.')
                    acc.append(f"{pos['title'].upper()}\n{pos['period']}\n{time}\n{description[0]}\n{pos['href']}\n")
    acc_string = '\n'.join(acc)
    return acc_string


html = get_html(URL)
items = get_content(html.text)
restaurant_obj_text = get_text_restaurant_parser(items)
rest_list = get_rest_list(items)
bar_list = get_bar_list(items)
# print(restaurant_obj_text)


