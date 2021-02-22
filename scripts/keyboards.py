from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('❇️ Акции и скидки')
    keyboard.row('🔔 Услуги', '🌐 Связь с нами')
    keyboard.row('🎪 Мероприятия', '🍽️ Питание')
    return keyboard


def food_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('🍽️ Рестораны')
    keyboard.row('🍸 Бары', '🌭 Снек-бары')
    keyboard.row('🍨 Детям')
    keyboard.row('🔙 Назад')
    return keyboard