import pickle

import telebot
from telebot.types import Message

from parsers.megaparser import parser_dict
from sripts import keyboards
from settings import TOKEN
from sripts.logging import log, configure_logging
from text_data import text_data


bot = telebot.TeleBot(TOKEN)

USERS_ID = set()

main_keyboard = keyboards.main_keyboard()
transfer_keyboard = keyboards.transfer_keyboard()
restaurant_keyboard = keyboards.restarurant_keyboard()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text_data['instruction']['start'], reply_markup=main_keyboard)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, text_data['instruction']['help'], reply_markup=main_keyboard)


@bot.message_handler(commands=['awards'])
def message_awards(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
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

        elif word in text_data['eat_list']:
            bot.send_message(message.chat.id, f'Вы можете выбрать одно из наших заведений:\n\n',
                             reply_markup=restaurant_keyboard)

    if message.text.lower() == '🔙 назад':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_keyboard)

    elif message.text.lower() == '📰 новости':
        bot.send_message(message.chat.id, parser_dict['news_parser'], reply_markup=main_keyboard,
                         disable_web_page_preview=True)

    elif message.text.lower() == 'рестораны и бары':
        bot.send_message(message.chat.id, 'Рестораны и бары', reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'рестораны':
        bot.send_message(message.chat.id, f'{parser_dict["restaurant_parser"][0]}\n'
                                          f'{parser_dict["restaurant_parser"][1]}\n', reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'бары':
        bot.send_message(message.chat.id, f'{parser_dict["restaurant_parser"][2]}\n'
                                          f'{parser_dict["restaurant_parser"][3]}\n'
                                          f'{parser_dict["restaurant_parser"][4]}\n'
                                          f'{parser_dict["restaurant_parser"][5]}\n', reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'детям':
        bot.send_message(message.chat.id, f'{parser_dict["restaurant_parser"][6]}\n', reply_markup=restaurant_keyboard)

    elif message.text.lower() == '❇️ акции и скидки':
        bot.send_message(message.chat.id, parser_dict['promotion_parser'], reply_markup=main_keyboard,
                         disable_web_page_preview=True)

    elif message.text.lower() == 'мероприятия':
        bot.send_message(message.chat.id, parser_dict['calendar_parser'], reply_markup=main_keyboard)

    elif message.text.lower() == 'трансфер':
        bot.send_message(message.chat.id, 'Заказать трансфер: 88002507797', reply_markup=transfer_keyboard)

    elif message.text.lower() == 'контакты':
        bot.send_message(message.chat.id, 'Звоните по номеру: 8800200600', reply_markup=main_keyboard)


configure_logging()
bot.polling()
