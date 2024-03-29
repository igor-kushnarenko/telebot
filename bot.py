import time

import telebot
from telebot.types import Message

import parsers.schedule_parser
from scripts.add_user import add_user, read_user_set
from parsers.megaparser import parser_dict
from settings import TOKEN
from scripts import keyboards
from scripts.logg import log, configure_logging
from scripts.text_data import text_data

bot = telebot.TeleBot(TOKEN)
main_keyboard = keyboards.main_keyboard()
food_keyboard = keyboards.food_keyboard()
schedule_keyboard = keyboards.schedule_keyboard()
contacts_keyboard = keyboards.contacts_keyboard()
services_keyboard = keyboards.services_keyboard()
teen_club_keyboard = keyboards.teen_club_keyboard()
cook_masterclass_keyboard = keyboards.cook_masterclass_keyboard()
fedorova_keyboard = keyboards.fedorova_keyboard()


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
    print(f'{message.from_user.id}, {message.from_user.first_name} => {message.text}')

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
    elif message.text == '🗓️ Расписание/Мастер-классы':
        bot.send_message(
            message.chat.id,
            text='C 1 июня по 31 августа в сети курортов Alean Family Resort Collection будут работать '
                 'творческие мастерские выставки, на которых все желающие могут приобрести детские поделки, '
                 'а так же принять участие в благотворительных аукционах, и все собранные средства будут направленны '
                 'в благотворительный фонд Оксаны Федоровой.',
            reply_markup=fedorova_keyboard,
            disable_web_page_preview=True,
        )
        bot.send_message(
            message.chat.id,
            text='Выберите расписание: ',
            reply_markup=schedule_keyboard,
            disable_web_page_preview=True,
        )
    elif message.text == '🎆 Вечерние мероприятия':
        file = parsers.schedule_parser.calendar_open_image()
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
        image_name = 'kulinarny_master_class.jpg'
        file = parsers.schedule_parser.schedule_open_img(image_name)
        try:
            image = open(file, 'rb')
            bot.send_photo(
                message.chat.id,
                image,
                reply_markup=schedule_keyboard,
            )
            bot.send_message(
                message.chat.id,
                text='Подробнее: ',
                reply_markup=cook_masterclass_keyboard,
            )
        except:
            bot.send_message(
                message.chat.id,
                text='Расписание не найдено',
                reply_markup=schedule_keyboard,
            )
    elif message.text == '🎥 Cinema-academy':
        image_name = 'kino.jpg'
        file = parsers.schedule_parser.schedule_open_img(image_name)
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
    elif message.text == '🤸 Fitness-academy':
        image_name = 'fitness.jpg'
        file = parsers.schedule_parser.schedule_open_img(image_name)
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
    elif message.text == '😎 Teen-club':
        bot.send_message(
            message.chat.id,
            text='Teen CLUB - это Клуб для тинейджеров, отдыхающих в Alean Family Resort & Spa Doville 5*',
            reply_markup=teen_club_keyboard,
        )

    elif message.text == '❇ Акции и скидки':
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
            reply_markup=services_keyboard,
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


if __name__ == '__main__':
    configure_logging()
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as ex:
            time.sleep(3)
            print(ex)
