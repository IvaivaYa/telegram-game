import telebot 
from telebot import types

#       https://t.me/for_coding_tg_game_bot
token = '6313330320:AAHEY7yOlocow6xs1jfwi_ZP8DlXxhLQK14'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    start_markup = types.InlineKeyboardMarkup()
    start_gaame_btn = types.InlineKeyboardButton(text = "Да, начать", callback_data="start_game")
    start_markup.add(start_gaame_btn)

    global name_of_user
    name_of_user = message.from_user.first_name

    bot.send_message(message.chat.id, f"Привет, {name_of_user}!\
                    \nТы хочешь начать игру?", reply_markup = start_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_processing(callback_mess):
    if callback_mess.data == 'start_game':
        bot.send_message(callback_mess.message.chat.id, 'Отлично! Тогда начинаем')

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, f"{name_of_user} написал: {message.text}")

bot.infinity_polling()