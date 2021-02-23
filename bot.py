import telebot
from telebot.types import Message

from add_user import add_user
from parsers.megaparser import parser_dict
from scripts import keyboards
from settings import TOKEN
from scripts.logg import log, configure_logging
from text_data import text_data


bot = telebot.TeleBot(TOKEN)
main_keyboard = keyboards.main_keyboard()
food_keyboard = keyboards.food_keyboard()
schedule_keyboard = keyboards.schedule_keyboard()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # add_user(message.from_user.id) # todo здесь проблема когда начинает писать новый юзер
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

    elif message.text == '❇️ Акции и скидки':
        bot.send_message(
            message.chat.id,
            text=parser_dict['promotion_parser'],
            reply_markup=main_keyboard,
            disable_web_page_preview=True,
        )

    elif message.text == '🎪 Мероприятия':
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

    elif message.text == '🌐 Связь с нами':
        bot.send_message(
            message.chat.id,
            text=text_data['contacts'],
            reply_markup=main_keyboard,
            disable_web_page_preview=True,
        )

    elif message.text == '🔔 Услуги':
        bot.send_message(
            message.chat.id,
            text=text_data['services'],
            reply_markup=main_keyboard,
            disable_web_page_preview=True,
        )

    elif message.text == '🔙 Назад':
        bot.send_message(
            message.chat.id,
            text='Главное меню',
            reply_markup=main_keyboard,
        )

    # заготовка для статистикаи бота
    # if message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
    #     st = message.text.split(' ')
    #     if 'txt' in st or 'тхт' in st:
    #         tg_analytic.analysis(st,message.chat.id)
    #         with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
    #             bot.send_document(message.chat.id,file)
    #         tg_analytic.remove(message.chat.id)
    #     else:
    #         messages = tg_analytic.analysis(st,message.chat.id)
    #         bot.send_message(message.chat.id, messages)

    else:
        bot.send_message(
            message.chat.id,
            text=text_data['instruction']['help'],
            reply_markup=main_keyboard,
            disable_web_page_preview=True,
        )


configure_logging()
bot.polling()
