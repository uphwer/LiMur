# git clone https://github.com/eternnoir/pyTelegramBotAPI.git
# cd pyTelegramBotAPI
# python setup.py install
import telebot
from telebot import types
import PIL
import random
import os
bot = telebot.TeleBot('5828640605:AAHQ-VQJrWNQ_LLJ3kbYzLpDCNostqdBi4o')


@bot.message_handler(commands=["help"])
def help(message):
    photo = open()
    bot.send_message(message.chat.id, "Список команд бота:\n"
                                      "/start — Запустить бота\n"
                                      "/main — Главное меню\n"
                                      "/about — Узнать больше про бота")

@bot.message_handler(commands=["about"])
def about(message):
    bot.send_message(message.chat.id, "Интересно, как работают правила пунктуации в английском языке?\n"
                                      "Не проблема! Моя работа — научить тебя ей.\n"
                                      "Благодаря мне ты сможешь узнать больше информации по интересующей тебя теме,\n"
                                      "А также попрактиковаться в ней.\n"
                                      "Так что, давай начнём!")

@bot.message_handler(commands=["start", 'main'])
def start(message):
    repmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    inmarkup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я — LiMur бот, помощник в изучении пунктуации английского языка!", reply_markup='')
    but_start = types.InlineKeyboardButton(text='Начать 🚀', callback_data='start')
    but_creators = types.InlineKeyboardButton(text='Создатели 💼', callback_data='creators')
    but_home = types.KeyboardButton('Главная 🏡')
    inmarkup.add(but_start, but_creators)
    repmarkup.add(but_home)
    bot.send_message(message.chat.id, "Выбери интересующий раздел:", reply_markup=repmarkup)
    bot.send_message(message.chat.id, "Начать — начать обучение\n"
                                      "Создатели — посмотреть создателей", reply_markup=inmarkup)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'start':
        markup = types.InlineKeyboardMarkup()
        but_oxf = types.InlineKeyboardButton(text='Оксфордская запятая', callback_data='oxford')
        markup.add(but_oxf)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выбери тему:', reply_markup=markup)
    elif call.data == 'creators':
        markup = types.InlineKeyboardMarkup()
        but_it = types.InlineKeyboardButton(text='Тимур🧑🏻‍💻', url='https://vk.com/g_timur')
        but_lingv = types.InlineKeyboardButton(text='Алина 👩🏻‍🏫', url='https://vk.com/allosse')
        markup.add(but_it, but_lingv)
        bot.send_message(call.message.chat.id, "Создатели бота:", reply_markup='')
        bot.send_message(call.message.chat.id, "Программист — Тимур Гаффоров\n"
                                          "Лингвист — Алина Осинцева", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.strip() == 'Главная 🏡':
        start(message)
    else:
        cat = open('20141703160331.jpg', 'rb')
        bot.send_photo(message.chat.id, cat, 'Извини, я тебя не понял 😬')

print('Working...')
bot.infinity_polling()