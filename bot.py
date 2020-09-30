import telebot
from telebot.types import Message
from settings import TOKEN
from text_data import text_data
from megaparser import parser_dict
import pickle



import logging
log = logging.getLogger('bot')

bot = telebot.TeleBot(TOKEN)
STICKER_ID = 'CAACAgIAAxkBAAIHil90PAYckRQQH9qx1DfDZkgQiYZFAAI3AAPRYSgLtg532um5J84bBA'

USERS_ID = set()


def configure_logging():
    file_handler = logging.FileHandler('bot.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M'))
    file_handler.setLevel(logging.INFO)
    log.addHandler(file_handler)
    log.setLevel(logging.INFO)


def main_keyboard():
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Новости')
    keyboard1.row('Акции и скидки', 'Рестораны и бары')
    keyboard1.row('Трансфер', 'Контакты', 'Бронирование',)
    keyboard1.row('Мероприятия')
    return keyboard1


def transfer_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Бизнес', 'Премиум', 'Минивен')
    keyboard.row(('🔙 Назад'))
    return keyboard


def restarurant_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Рестораны', 'Бары', 'Детям')
    keyboard.row(('🔙 Назад'))
    return keyboard


main_keyboard = main_keyboard()
transfer_keyboard = transfer_keyboard()
restaurant_keyboard = restarurant_keyboard()


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
    print(f'{message.from_user.id}, {message.from_user.first_name} => {message.text}')

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

    elif message.text.lower() == 'новости':
        bot.send_message(message.chat.id, parser_dict['news_parser'], reply_markup=main_keyboard)

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

    elif message.text.lower() == 'акции и скидки':
        bot.send_message(message.chat.id, parser_dict['promotion_parser'], reply_markup=main_keyboard)

    elif message.text.lower() == 'мероприятия':
        bot.send_message(message.chat.id, parser_dict['calendar_parser'], reply_markup=main_keyboard)

    elif message.text.lower() == 'бронирование':
        bot.send_message(message.chat.id,
                         'https://booking.aleanfamily.ru/index.php?hotel=523', reply_markup=main_keyboard)

    elif message.text.lower() == 'трансфер':
        bot.send_message(message.chat.id, 'Заказать трансфер: 88002507797', reply_markup=transfer_keyboard)

    elif message.text.lower() == 'контакты':
        bot.send_message(message.chat.id, 'Звоните по номеру: 8800200600', reply_markup=main_keyboard)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)


configure_logging()
bot.polling()
