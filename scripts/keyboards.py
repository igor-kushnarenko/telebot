from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🗓️ Расписание мероприятий')
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
    keyboard.row('🥗 Кулинарный мастер-класс')
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




def schedule_open_img():
    directory = 'static/img'
    if number_week // 2 == 0:
        name_image = '2.jpg'
    else:
        name_image = '1.jpg'
    path_img = directory + '/' + name_image
    return path_img