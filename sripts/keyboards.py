from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('📰 Новости')
    keyboard.row('❇️ Акции и скидки', '🍽️ Питание')
    keyboard.row('🔔 Услуги', '🗨️ Контакты')
    keyboard.row('🎪 Мероприятия')
    return keyboard