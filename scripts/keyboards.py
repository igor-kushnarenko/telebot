from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🎪 Мероприятия')
    keyboard.row('🍽️ Питание', '🔔 Услуги')
    keyboard.row('❇️ Акции и скидки', '🌐 Связь с нами')
    return keyboard


def food_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🍽️ Рестораны', '🍸 Бары')
    keyboard.row('🌭 Снек-бары', '🍨 Детям')
    keyboard.row('🔙 Назад')
    return keyboard