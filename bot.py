import pickle

import telebot
from telebot.types import Message
from telebot import types

from parsers.megaparser import parser_dict
from sripts import keyboards
from settings import TOKEN
from sripts.logging import log, configure_logging
from text_data import text_data


bot = telebot.TeleBot(TOKEN)

USERS_ID = set()

main_keyboard = keyboards.main_keyboard()



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text_data['instruction']['start'], reply_markup=main_keyboard)





@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, text_data['instruction']['help'], reply_markup=main_keyboard)


@bot.message_handler(commands=['awards'])
def message_awards(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        'Проголосовать', url='https://www.luxuryhotelawards.com/hotel/alean-family-resort-spa-doville/'))
    bot.send_message(
        message.chat.id, text_data['awards'], reply_markup=keyboard)





@bot.message_handler(content_types=['text'])
def inline_key(message: Message):

    log.info(f'{message.from_user.id}, {message.from_user.first_name} => {message.text}')

    text = message.text.lower()
    text_list = text.split(' ')
    for word in text_list:
        if word in text_data['hello_list']:
            answer = 'Добрый день! Для начала работы нажмите /start\nДля помощи, нажмите /help\n'

            with open('user_id.pickle', 'rb') as f:
                USERS_ID = pickle.load(f)
            if message.from_user.id in USERS_ID:
                answer = f'Рад видеть Вас снова {message.from_user.first_name}!\n' \
                         f'Для начала работы нажмите /start\nДля помощи, нажмите /help\n'
            bot.send_message(message.chat.id, f'{answer}', reply_markup=main_keyboard)
            USERS_ID.add(message.from_user.id)
            with open('user_id.pickle', 'wb') as f:
                pickle.dump(USERS_ID, f)

        elif word in text_data['goodbye_list']:
            bot.send_message(message.chat.id, 'До новых встреч!')

    if message.text == '🍽️ Питание':
        keyboard_inline = types.InlineKeyboardMarkup()
        item_normandie = types.InlineKeyboardButton(text='Ресторан "Normandie"', callback_data='normandie')
        item_san_michel = types.InlineKeyboardButton(text='Ресторан "Saint Michel"', callback_data='san_michel')
        item_bon_appetit = types.InlineKeyboardButton(text='Снек-бар "Bon appetit"', callback_data='bon_appetit')
        item_marinie = types.InlineKeyboardButton(text='Снек-бар "Marinie"', callback_data='marinie')
        item_le_paradis = types.InlineKeyboardButton(text='Снек-бар "le Paradis"', callback_data='le_paradis')
        item_caramel = types.InlineKeyboardButton(text='Детское кафе "Карамелька"', callback_data='caramel')
        keyboard_inline.add(
            item_normandie, item_san_michel, item_bon_appetit,
            item_marinie, item_caramel, item_le_paradis, row_width=2)
        bot.send_message(message.chat.id, 'Выберите заведение', reply_markup=keyboard_inline)

    elif message.text == '📰 Новости':
        bot.send_message(message.chat.id, parser_dict['news_parser'], reply_markup=main_keyboard,
                         disable_web_page_preview=True)

    elif message.text == '❇️ Акции и скидки':
        bot.send_message(message.chat.id, parser_dict['promotion_parser'], reply_markup=main_keyboard,
                         disable_web_page_preview=True)

    elif message.text == '🎪 Мероприятия':
        bot.send_message(message.chat.id, parser_dict['calendar_parser'], reply_markup=main_keyboard)

    elif message.text == '🗨️ Контакты':
        bot.send_message(message.chat.id, 'Звоните по номеру: 8800200600', reply_markup=main_keyboard)



configure_logging()
bot.polling()
