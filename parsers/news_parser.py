import requests
from bs4 import BeautifulSoup
import fake_useragent

HOST = 'https://dovilleresort.ru/'
URL = 'https://dovilleresort.ru/news/'
user = fake_useragent.FakeUserAgent().random
HEADERS = {'user_agent': user}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='cards__item col-md-4 col-sm-6')
    data = []

    for item in items:
        data.append(
            {
                'title': item.find('div', class_='cards__header').get_text(strip=True),
                'date': item.find('div', class_='cards__detail').get_text(strip=True),
                'desc': item.find('div', class_='cards__caption').get_text(strip=True),
                'href': HOST + item.find('a', class_='btn btn-block cards__btn').get('href'),
            }
        )
    return data


def get_text_news_parser(items):
    acc = []
    for i in items[:3]:
        acc.append(f"{i['title'].upper()}\n{i['date']}\n{i['desc']}\n{i['href']}")
    acc_string = '\n\n'.join(acc)
    return acc_string


html = get_html(URL)
items = get_content(html.text)
news_obj_text = get_text_news_parser(items)


