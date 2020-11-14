time_dict = {
    'РЕСТОРАН NORMANDIE': '08:00 - 20:00',
    'ГАСТРОНОМИЧЕСКИЙ РЕСТОРАН SAINT MICHEL': '12:00 - 00:00',
    'DISCO BAR': '20:00 - 02:00',
    'СНЕК-БАР MARINIE': '10:00 - 00:00',
    'LOBBY BAR': 'Круглосуточно',
}


# import requests
# from bs4 import BeautifulSoup as bs4
# import fake_useragent
#
# HOST = 'https://dovilleresort.ru'
# URL = 'https://dovilleresort.ru/restaurant/'
# user = fake_useragent.FakeUserAgent().random
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'user_agent': user
# }
#
#
# def get_url(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
#
# def get_content(html):
#     soup = bs4(html, 'html.parser')
#     items = soup.find_all('div', class_='col-md-4 col-sm-6 col-centered col-restaurant')
#     url_dict = {}
#     for item in items:
#         sub_url = (item.find('a').get('href'))
#         url = HOST + sub_url
#         r = requests.get(url, headers=HEADERS, params='')
#         soup = bs4(r.text, 'html.parser')
#         items = soup.find_all('div', class_='body')
#         for item in items:
#             name = item.find(id='pagetitle').get_text()
#             date = item.find_all('div', class_='restaurant-detail')
#             for i in date:
#                 if i.find('br') != None:
#                     print(i.find('br').get_text())
#
#
# html = get_url(URL)
# get_content(html.text)