import telebot
from telebot import types
import random


bot = telebot.TeleBot('5970858471:AAG4wuaaN51u0C36qg0M-oaCQYy3sJf1D98')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(commands=['info'])
def start(message):
    aaa=random.randint(0, 1)
    if aaa==1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, "Я бот созданный для группы", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, "Я бот не созданный для группы", reply_markup=markup)





bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
