import sys
import time

import telebot
from telebot.types import Message

import schedule_parser
from scripts.add_user import add_user, read_user_set
from parsers.megaparser import parser_dict
from settings import TOKEN
from scripts import keyboards
from scripts.logg import log, configure_logging
from text_data import text_data

bot = telebot.TeleBot(TOKEN)
main_keyboard = keyboards.main_keyboard()
food_keyboard = keyboards.food_keyboard()
schedule_keyboard = keyboards.schedule_keyboard()
contacts_keyboard = keyboards.contacts_keyboard()
services_keydoars = keyboards.services_keyboard()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    add_user(message)
    bot.send_message(
        message.chat.id,
        text_data['instruction']['start'],
        reply_markup=main_keyboard
    )


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id,
        text_data['instruction']['help'],
        reply_markup=main_keyboard,
    )


@bot.message_handler(content_types=['text'])
def inline_key(message: Message):
    log.info(f'{message.from_user.id}, {message.from_user.first_name} => {message.text}')

    # ПИТАНИЕ
    if message.text == '🍽️ Питание':
        bot.send_message(
            message.chat.id,
            text='Выберите категорию: ',
            reply_markup=food_keyboard,
        )
    elif message.text == '🍽️ Рестораны':
        bot.send_message(
            message.chat.id,
            text=parser_dict['rest_list'],
            reply_markup=food_keyboard,
            disable_web_page_preview=True,
        )
    elif message.text == '🍸 Бары':
        bot.send_message(
            message.chat.id,
            text=parser_dict['bar_list'],
            reply_markup=food_keyboard,
            disable_web_page_preview=True,
        )
    elif message.text == '🌭 Снек-бары':
        bot.send_message(
            message.chat.id,
            text=parser_dict['sneck_list'],
            reply_markup=food_keyboard,
            disable_web_page_preview=True,
        )
    elif message.text == '🍨 Детям':
        bot.send_message(
            message.chat.id,
            text=parser_dict['child_list'],
            reply_markup=food_keyboard,
            disable_web_page_preview=True,
        )

    # РАСПИСАНИЕ
    elif message.text == '🗓️ Расписание мероприятий':
        bot.send_message(
            message.chat.id,
            text='Выберите расписание:',
            reply_markup=schedule_keyboard,
        )
    elif message.text == '7️⃣ Расписание на 7 дней':
        bot.send_message(
            message.chat.id,
            text=parser_dict['calendar_parser'],
            reply_markup=schedule_keyboard,
        )
    elif message.text == '🎆 Вечерние мероприятия':
        image_name = 'animation_week.jpg'
        file = schedule_parser.schedule_open_img(image_name)
        try:
            image = open(file, 'rb')
            bot.send_photo(
                message.chat.id,
                image,
                reply_markup=schedule_keyboard,
            )
        except:
            bot.send_message(
                message.chat.id,
                text='Расписание не найдено',
                reply_markup=schedule_keyboard,
            )
    elif message.text == '☀️ Дневные мероприятия':
        bot.send_message(
            message.chat.id,
            text=schedule_parser.schedule_day_parser,
            reply_markup=schedule_keyboard,
            disable_web_page_preview=True,
        )
    elif message.text == '💻 Студия 3D-моделирования':
        IMAGE_NAME = 'media_studio.jpg'
        file = schedule_parser.schedule_open_img(IMAGE_NAME)
        try:
            image = open(file, 'rb')
            bot.send_photo(
                message.chat.id,
                image,
                reply_markup=schedule_keyboard,
            )
        except:
            bot.send_message(
                message.chat.id,
                text='Расписание не найдено',
                reply_markup=schedule_keyboard,
            )
    elif message.text == '🥗 Кулинарный мастер-класс':
        IMAGE_NAME = 'kulinarny_master_class.jpg'
        file = schedule_parser.schedule_open_img(IMAGE_NAME)
        try:
            image = open(file, 'rb')
            bot.send_photo(
                message.chat.id,
                image,
                reply_markup=schedule_keyboard,
            )
        except:
            bot.send_message(
                message.chat.id,
                text='Расписание не найдено',
                reply_markup=schedule_keyboard,
            )

    elif message.text == '❇️ Акции и скидки':
        bot.send_message(
            message.chat.id,
            text=parser_dict['promotion_parser'],
            reply_markup=main_keyboard,
            disable_web_page_preview=True,
        )

    elif message.text == '🌐 Связь с нами':
        bot.send_message(
            message.chat.id,
            text=text_data['contacts'],
            reply_markup=contacts_keyboard,
        )

    elif message.text == '🔔 Услуги':
        bot.send_message(
            message.chat.id,
            text='Наши услуги: ',
            reply_markup=services_keydoars,
        )

    elif message.text == '🔙 Назад':
        bot.send_message(
            message.chat.id,
            text='Главное меню',
            reply_markup=main_keyboard,
        )

    elif message.text == 'Статистика':
        answer = read_user_set()
        bot.send_message(
            message.chat.id,
            text=answer,
            reply_markup=main_keyboard,
        )

    else:
        bot.send_message(
            message.chat.id,
            text=text_data['instruction']['help'],
            reply_markup=main_keyboard,
            disable_web_page_preview=True,
        )


def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    configure_logging()
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
