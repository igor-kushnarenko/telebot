import telebot
from telebot import types
from settings import TOKEN
from promotion_parser import obj_text
from restaurant_parser import restaurant_obj_text
from calendar_parser import calendar_obj_text
from news_parser import news_obj_text

bot = telebot.TeleBot(TOKEN)


def keyboard_menu():
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Новости')
    keyboard1.row('Акции и скидки', 'Бронирование', 'Мероприятия')
    keyboard1.row('Трансфер', 'Рестораны и бары', 'Контакты')
    return keyboard1


def transfer_menu():
    transfer_keyboard = telebot.types.ReplyKeyboardMarkup()
    transfer_keyboard.row('Бизнес', 'Премиум', 'Минивен')
    transfer_keyboard.row(('Назад'))
    return transfer_keyboard


main_keyboard = keyboard_menu()
transfer_keyboard = transfer_menu()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=main_keyboard)


@bot.message_handler(content_types=['text'])
def inline_key(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Вас приветствует ифно-бот Alean Family Resort & SPA Doville! '
                                          'Что бы продолжить, нажмите меню.', reply_markup=main_keyboard)

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До новых встреч!')

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_keyboard)

    elif message.text.lower() == 'контакты':
        bot.send_message(message.chat.id, 'Звоните по номеру: 8800200600')

    elif message.text.lower() == 'акции и скидки':
        for text in obj_text:
            bot.send_message(message.chat.id, text)

    elif message.text.lower() == 'мероприятия':
        for text in calendar_obj_text:
            bot.send_message(message.chat.id, text)

    elif message.text.lower() == 'рестораны и бары':
        bot.send_message(message.chat.id, restaurant_obj_text)

    elif message.text.lower() == 'бронирование':
        bot.send_message(message.chat.id, 'https://booking.aleanfamily.ru/index.php?hotel=523')

    elif message.text.lower() == 'трансфер':
        bot.send_message(message.chat.id, 'Заказать трансфер: 88002507797', reply_markup=transfer_keyboard)

    elif message.text.lower() == 'новости':
        bot.send_message(message.chat.id, news_obj_text)


bot.polling()
