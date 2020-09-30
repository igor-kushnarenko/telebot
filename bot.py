import telebot
from telebot.types import Message

from settings import TOKEN
from promotion_parser import obj_text
from restaurant_parser import restaurant_obj_text
from calendar_parser import calendar_obj_text
from news_parser import news_obj_text
from text_data import text_data

bot = telebot.TeleBot(TOKEN)
STICKER_ID = 'CAACAgIAAxkBAAIHil90PAYckRQQH9qx1DfDZkgQiYZFAAI3AAPRYSgLtg532um5J84bBA'
USERS_ID = set()


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
    keyboard.row(('Назад'))
    return keyboard


def restarurant_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Рестораны', 'Бары', 'Детям')
    keyboard.row(('Назад'))
    return keyboard


def back_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row(('Назад'))
    return keyboard


main_keyboard = main_keyboard()
transfer_keyboard = transfer_keyboard()
restaurant_keyboard = restarurant_keyboard()
back_keyboard = back_keyboard()


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
        message.chat.id,
        'Второй год подряд пятизвездочный курорт Alean Family Resort & Spa Doville '
        'номинирован на международную премию World Luxury Hotel Awards. \n' +
        'Поддержать нас очень просто: \n' +
        '1) Перейдите по ссылке премии в модуль голосования.\n' +
        '2) Во второй строке выберите одну из трех номинаций. \n' +
        '3) Введите свой электронный адрес. \n' +
        '4) Нажмите кнопку Vote for this hotel. \n', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def inline_key(message: Message):
    text = message.text.lower()
    text_list = text.split(' ')
    print(text_list)
    for word in text_list:

        if word in text_data['hello_list']:
            answer = 'Добрый день! Для начала работы нажмите /start\nДля помощи, нажмите /help\n'
            if message.from_user.id in USERS_ID:
                answer = f'Рад видеть Вас снова {message.from_user.first_name}!\n' \
                         f'Для начала работы нажмите /start\nДля помощи, нажмите /help\n'
            bot.send_message(message.chat.id, f'{answer}', reply_markup=main_keyboard)
            USERS_ID.add(message.from_user.id)

        elif word in text_data['goodbye_list']:
            bot.send_message(message.chat.id, 'До новых встреч!')

        elif word in text_data['eat_list']:
            bot.send_message(message.chat.id, f'Вы можете пообедать в одном из наших заведений:\n\n'
                                              f' {restaurant_obj_text}', reply_markup=restaurant_keyboard)

        elif message.text.lower() == 'назад':
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_keyboard)

        elif message.text.lower() == 'новости':
            bot.send_message(message.chat.id, news_obj_text, reply_markup=main_keyboard)

        elif message.text.lower() == 'рестораны и бары':
            bot.send_message(message.chat.id, 'Рестораны и бары', reply_markup=restaurant_keyboard)

        elif message.text.lower() == 'рестораны':
            bot.send_message(message.chat.id, restaurant_obj_text[:375], reply_markup=restaurant_keyboard)

        elif message.text.lower() == 'бары':
            bot.send_message(message.chat.id, 'Бары', reply_markup=restaurant_keyboard)

        elif message.text.lower() == 'детям':
            bot.send_message(message.chat.id, 'Детям', reply_markup=restaurant_keyboard)

        elif message.text.lower() == 'акции и скидки':
            bot.send_message(message.chat.id, obj_text, reply_markup=main_keyboard)

        elif message.text.lower() == 'мероприятия':
            bot.send_message(message.chat.id, calendar_obj_text, reply_markup=main_keyboard)

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


bot.polling()
