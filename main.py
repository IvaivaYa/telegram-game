import telebot 
from telebot import types

token = 'токен'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()