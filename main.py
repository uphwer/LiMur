# git clone https://github.com/eternnoir/pyTelegramBotAPI.git
# cd pyTelegramBotAPI
# python setup.py install
import telebot
from telebot import types
bot = telebot.TeleBot('5828640605:AAHQ-VQJrWNQ_LLJ3kbYzLpDCNostqdBi4o')


@bot.message_handler(commands=["help"])
def help(message):
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
    elif call.data == 'oxford':
        markup = types.InlineKeyboardMarkup()
        but_oxfex = types.InlineKeyboardButton(text='Примеры', callback_data='oxfex1')
        but_oxf1 = types.InlineKeyboardButton(text='Упражнение №1', callback_data='oxf1')
        but_oxf2 = types.InlineKeyboardButton(text='Упражнение №2', callback_data='oxf2')
        but_back = types.InlineKeyboardButton(text='Назад', callback_data='start')
        markup.add(but_oxfex, but_oxf1, but_oxf2)
        markup.add(but_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Оксфордская запятая.\n'
                                                                                             'Оскфордская запятая (Oxford comma) — запятая, ставящаяся перед союзами and, or или nor,\n'
                                                                                             'а также перед последним пунктом в списке перечисляемых элементов.', reply_markup=markup)
    elif call.data == 'oxfex1':
        markup = types.InlineKeyboardMarkup()
        but_oxfnex = types.InlineKeyboardButton(text='Следущая страница >>', callback_data='oxfex2')
        markup.add(but_oxfnex)
        ex1 = open('photos/example-1.jpg', 'rb')
        bot.send_photo(call.message.chat.id, ex1, 'We invited the rhinoceri, Washington, and Lincoln.\n'
                                                  '– Мы пригласили носорогов, Вашингтона и Линкольна.\n'
                                                  '\n'
                                                  'В этом предложении присутствует оксфордская запятая.\n'
                                                  'Благодаря ей мы понимаем, что на мероприятие должны прийти два человека (Вашингтон и Линкольн) и носороги.\n'
                                                  'Зачем там носороги – это уже другой вопрос.', reply_markup=markup)
    elif call.data == 'oxfex2':
        markup = types.InlineKeyboardMarkup()
        but_oxfnex1 = types.InlineKeyboardButton(text='Упражнение №1', callback_data='oxf1')
        but_oxfnex2 = types.InlineKeyboardButton(text='Упражнение №2', callback_data='oxf2')
        markup.add(but_oxfnex1, but_oxfnex2)
        ex2 = open('photos/example-2.jpg', 'rb')
        bot.send_photo(call.message.chat.id, ex2, 'We invited the rhinoceri, Washington and Lincoln.\n'
                                                  '– Мы пригласили носорогов: Вашингтона и Линкольна.\n'
                                                  '\n'
                                                  'Запятая в английском предложении выполняет функцию двоеточия или тире.\n'
                                                  'В этом предложении отсутствие оксфордской запятой совершенно меняет смысл:\n'
                                                  'на мероприятие должны прийти носороги по имени Вашингтон и Линкольн.', reply_markup=markup)
    elif call.data == 'oxf1':
        markup = types.InlineKeyboardMarkup()
        but_ex1 = types.InlineKeyboardButton(text='К заданиям >>', callback_data='oxfexs1')

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.strip() == 'Главная 🏡':
        start(message)
    else:
        cat = open('photos/20141703160331.jpg', 'rb')
        bot.send_photo(message.chat.id, cat, 'Извини, я тебя не понял 😬')

print('Working...')
bot.infinity_polling()