import telebot


def main_keyboard():
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('📰 Новости')
    keyboard1.row('❇️ Акции и скидки', '🍽️ Рестораны и бары')
    keyboard1.row('🔔 Услуги', '🗨️ Контакты')
    keyboard1.row('🎪 Мероприятия')
    return keyboard1


def restarurant_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Рестораны', 'Бары', 'Детям')
    keyboard.row(('🔙 Назад'))
    return keyboard