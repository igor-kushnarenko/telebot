import telebot
from settings import TOKEN
from promotion_parser import obj_text
from restaurant_parser import restaurant_obj_text
from calendar_parser import calendar_obj_text
from news_parser import news_obj_text
from text_data import hello_list, gooby_list

bot = telebot.TeleBot(TOKEN)


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
    bot.reply_to(message, "Что бы начать работу с ботом, нажмите меню.", reply_markup=main_keyboard)


@bot.message_handler(commands=['awards'])
def help_command(message):
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
def inline_key(message):

    if message.text.lower() in hello_list:
        bot.send_message(message.chat.id,
                         'Вас приветствует ифно-бот Alean Family Resort & SPA Doville! '
                         'Что бы продолжить, нажмите меню. \n\n'
                         '🎉 Поддержите нас в номинации международной премии World Luxury Hotel Awards!!! 🎉 \n'
                         'Для этого нажмите /awards',
                         reply_markup=main_keyboard)

    elif message.text.lower() in gooby_list:
        bot.send_message(message.chat.id, 'До новых встреч!')

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_keyboard)

    elif message.text.lower() == 'новости':
        bot.send_message(message.chat.id, news_obj_text)

    elif message.text.lower() == 'рестораны и бары':
        bot.send_message(message.chat.id, 'Рестораны и бары', reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'рестораны':
        bot.send_message(message.chat.id, restaurant_obj_text[:375], reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'бары':
        bot.send_message(message.chat.id, 'Бары', reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'детям':
        bot.send_message(message.chat.id, 'Детям', reply_markup=restaurant_keyboard)

    elif message.text.lower() == 'акции и скидки':
        bot.send_message(message.chat.id, obj_text)

    elif message.text.lower() == 'мероприятия':
        bot.send_message(message.chat.id, calendar_obj_text)

    elif message.text.lower() == 'бронирование':
        bot.send_message(message.chat.id, 'https://booking.aleanfamily.ru/index.php?hotel=523')

    elif message.text.lower() == 'трансфер':
        bot.send_message(message.chat.id, 'Заказать трансфер: 88002507797', reply_markup=transfer_keyboard)

    elif message.text.lower() == 'контакты':
        bot.send_message(message.chat.id, 'Звоните по номеру: 8800200600')


bot.polling()
