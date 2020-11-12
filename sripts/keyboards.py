from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(True, True)
    # keyboard.row('🏨 Номера и цены')
    keyboard.row('❇️ Акции и скидки')
    keyboard.row('🔔 Услуги', '🌐 Связь с нами')
    keyboard.row('🎪 Мероприятия', '🍽️ Питание')
    return keyboard