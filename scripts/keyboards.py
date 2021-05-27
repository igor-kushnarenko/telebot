from telebot import types

from scripts.logg import log, configure_logging


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🗓️ Расписание/Мастер-классы')
    keyboard.row('🍽️ Питание', '🔔 Услуги')
    keyboard.row('❇ Акции и скидки', '🌐 Связь с нами')
    return keyboard


def food_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🍽️ Рестораны', '🍸 Бары')
    keyboard.row('🌭 Снек-бары', '🍨 Детям')
    keyboard.row('🔙 Назад')
    return keyboard


def schedule_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🎆 Вечерние мероприятия')
    keyboard.row('😎 Teen-club', '🥗 Кулинарный мастер-класс')
    keyboard.row('🎥 Cinema-academy', '🤸 Fitness-academy')
    keyboard.row('🔙 Назад')
    return keyboard


def contacts_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(
        types.InlineKeyboardButton('🔗 Instagram', 'https://www.instagram.com/doville__animation/'),
        types.InlineKeyboardButton('🔗 ВКОНТАКТЕ', 'https://vk.com/dovilleanimation_club'),
    )
    return keyboard


def services_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(
        types.InlineKeyboardButton('🛍️ Магазины', 'https://dovilleresort.ru/about/services/magazini/'),
        types.InlineKeyboardButton('💼 Консьерж', 'https://dovilleresort.ru/about/services/consierge/'),
        types.InlineKeyboardButton('🥘 Рум-сервис', 'https://dovilleresort.ru/about/services/room-service/'),
        types.InlineKeyboardButton('🅿️ Парковка', 'https://dovilleresort.ru/about/services/parking/'),
    )
    return keyboard


def teen_club_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(
        types.InlineKeyboardButton('Перейти ➡️', 'https://vk.com/public204655046'),
    )
    return keyboard


def cook_masterclass_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(
        types.InlineKeyboardButton('Перейти ➡️', 'https://www.instagram.com/stanislavkalinovskiy/'),
    )
    return keyboard


def fedorova_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(
        types.InlineKeyboardButton('Принять участие ➡️',
                                   'https://c.cloudpayments.ru/payments/7e8d475280974ced8aca998d76a93d60',
                                   callback_data='fedorova'),
    )
    return keyboard
