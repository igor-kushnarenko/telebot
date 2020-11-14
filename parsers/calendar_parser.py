import requests
from bs4 import BeautifulSoup
from datetime import datetime
import fake_useragent

URL = 'https://dovilleresort.ru/afisha/?date=1604188800'
HOST = 'https://dovilleresort.ru/'
user = fake_useragent.FakeUserAgent().random

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user_agent': user
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_=('calendar-table-item__inner calendar-table-item__inner_thematic js-poster-open',
                                       'calendar-table-item__inner calendar-table-item__inner_simple js-poster-open',
                                       'calendar-table-item__inner calendar-table-item__inner_ js-poster-open',
                                       'calendar-table-item__inner calendar-table-item__inner_holiday js-poster-open', ))
    # print(items)
    data = []
    for item in items:
        data.append(
            {
                'data': item.find('span', class_='js-poster-date').get_text(strip=True),
                'week_day': item.find('div', class_='calendar-table-item__weekday js-poster-week').get_text(strip=True),
                'title': item.find('div', class_='calendar-table-item__title').get_text(strip=True),
            }
        )
    return data


def get_text_calendar_parser(items):
    current_datetime = datetime.now()
    acc = []
    for pos in items[22:29]:
        acc.append(f"{pos['data']}, {pos['week_day']} - '{pos['title'].upper()}'\n")
    acc_string = '\n'.join(acc)
    # print(acc_string)
    return acc_string


html = get_html(URL)
items = get_content(html.text)
calendar_obj_text = get_text_calendar_parser(items)