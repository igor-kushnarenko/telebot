from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🗓️ Расписание мероприятий')
    keyboard.row('🍽️ Питание', '🔔 Услуги')
    keyboard.row('❇️ Акции и скидки', '🌐 Связь с нами')
    return keyboard


def food_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🍽️ Рестораны', '🍸 Бары')
    keyboard.row('🌭 Снек-бары', '🍨 Детям')
    keyboard.row('🔙 Назад')
    return keyboard


def schedule_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('7️⃣ Расписание на 7 дней')
    keyboard.row('🎆 Вечерние мероприятия')
    keyboard.row('💻 Студия 3D-моделирования')
    keyboard.row('🥗 Кулинарный мастер-класс')
    keyboard.row('🔙 Назад')
    return keyboard


def contacts_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(
        types.InlineKeyboardButton('Instagram', 'https://www.instagram.com/doville__animation/'),
        types.InlineKeyboardButton('VK', 'https://vk.com/dovilleanimation_club'),
    )