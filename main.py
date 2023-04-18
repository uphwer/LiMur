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
    but_start = types.InlineKeyboardButton(text='Начать 🚀', callback_data='start')
    but_creators = types.InlineKeyboardButton(text='Создатели 💼', callback_data='creators')
    but_home = types.KeyboardButton('Главная 🏡')
    inmarkup.add(but_start, but_creators)
    repmarkup.add(but_home)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я — LiMur бот, помощник в изучении пунктуации английского языка!", reply_markup=repmarkup)
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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_ex1 = types.KeyboardButton("К заданиям 🌟")
        but_main = types.KeyboardButton("Главная 🏡")
        markup.add(but_ex1)
        markup.add(but_main)
        bot.send_message(call.message.chat.id, 'Упражнение №1\n'
                                               '\n'
                                               'Упражнение заключается в правильной постановке запятой.\n'
                                               'Будет дано предложение с изображением, надо переписать предложение с запятой или без, в зависимости от смысла.', reply_markup=markup)
    elif call.data == 'oxf2':
        markup = types.InlineKeyboardMarkup()
        but_next = types.InlineKeyboardButton(text='Далее >>', callback_data='oxf_ex2.1')
        markup.add(but_next)
        bot.send_message(call.message.chat.id, 'Упражнение №2\n'
                                               '\n'
                                               'Упражнение заключается в выборе подходящей картинки под предложение.\n'
                                               'Будет дано предложение и две фотографии. Надо будет выбрать подходящую.', reply_markup=markup)
    elif call.data == 'oxf_ex2.1':
        markup = types.InlineKeyboardMarkup()
        but_one = types.InlineKeyboardButton(text='1', callback_data='oxf_ex2.1cor')
        but_two = types.InlineKeyboardButton(text='2', callback_data='oxf_ex2.1incor')
        markup.add(but_one, but_two)
        photo1 = open('photos/prnt.jpg', 'rb')
        photo2 = open('photos/prnt1.jpg', 'rb')
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(photo1), telebot.types.InputMediaPhoto(photo2)])
        bot.send_message(call.message.chat.id, 'I love my parents, Lady Gaga, and Ryan Reynolds.', reply_markup=markup)

    elif call.data == 'oxf_ex2.1incor':
        markup = types.InlineKeyboardMarkup()
        but_return = types.InlineKeyboardButton(text='<< Назад', callback_data='oxf_ex2.1')
        markup.add(but_return)
        bot.send_message(call.message.chat.id, 'Неправильно, попробуй ещё раз!', reply_markup=markup)

    elif call.data == 'oxf_ex2.1cor':
        markup = types.InlineKeyboardMarkup()
        but_one = types.InlineKeyboardButton(text='1', callback_data='oxf_ex2.2incor')
        but_two = types.InlineKeyboardButton(text='2', callback_data='oxf_ex2.2cor')
        markup.add(but_one, but_two)
        photo1 = open('photos/police.jpg', 'rb')
        photo2 = open('photos/police1.png', 'rb')
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(photo1), telebot.types.InputMediaPhoto(photo2)])
        bot.send_message(call.message.chat.id, 'Steven turned and faced Susan, his sister, and a police officer.', reply_markup=markup)

    elif call.data == 'oxf_ex2.2incor':
        markup = types.InlineKeyboardMarkup()
        but_return = types.InlineKeyboardButton(text='<< Назад', callback_data='oxf_ex2.1cor')
        markup.add(but_return)
        bot.send_message(call.message.chat.id, 'Неправильно, попробуй ещё раз!', reply_markup=markup)

    elif call.data == 'oxf_ex2.2cor':
        markup = types.InlineKeyboardMarkup()
        but_back = types.InlineKeyboardButton(text='<< Назад', callback_data='ford')
        markup.add(but_back)
        photo1 = open('photos/full-length-portrait-of-a-confident-young-male-builder_171337-5191.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo1, 'Work in progress...', reply_markup=markup)

    elif call.data == 'ford':
        markup = types.InlineKeyboardMarkup()
        but_oxfex = types.InlineKeyboardButton(text='Примеры', callback_data='oxfex1')
        but_oxf1 = types.InlineKeyboardButton(text='Упражнение №1', callback_data='oxf1')
        but_oxf2 = types.InlineKeyboardButton(text='Упражнение №2', callback_data='oxf2')
        but_back = types.InlineKeyboardButton(text='Назад', callback_data='start')
        markup.add(but_oxfex, but_oxf1, but_oxf2)
        markup.add(but_back)
        bot.send_message(call.message.chat.id, 'Оксфордская запятая.\n'
                                                'Оскфордская запятая (Oxford comma) — запятая, ставящаяся перед союзами and, or или nor,\n'
                                                'а также перед последним пунктом в списке перечисляемых элементов.', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.strip() == 'Главная 🏡':
        start(message)
    elif message.text.strip() == 'К заданиям 🌟':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_main = types.KeyboardButton("Главная 🏡")
        markup.add(but_main)
        photo = open('photos/mmvxyri.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, 'Задание №1\n'
                                               '\n'
                                               'Timur photographed two ostriches, Timothy(,) and Max.', reply_markup=markup)
        bot.register_next_step_handler(message, oxf_ex1_num1)
    else:
        cat = open('photos/ty26hmpfe3f51.jpg', 'rb')
        bot.send_photo(message.chat.id, cat, 'Извини, я тебя не понял 😬')
def oxf_ex1_num1(message):
    if message.text.strip() == 'Timur photographed two ostriches, Timothy and Max.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_main = types.KeyboardButton("Главная 🏡")
        markup.add(but_main)
        photo = open('photos/people-chatting-house-party-3574393.jpg', 'rb')
        bot.send_message(message.chat.id, 'All right!')
        bot.send_photo(message.chat.id, photo, 'Задание №2\n'
                                               '\n'
                                               'Her friends, Steven(,) and Sarah, were present at the party.', reply_markup=markup)
        bot.register_next_step_handler(message, oxf_ex1_num2)
    elif message.text.strip() == 'Timur photographed two ostriches, Timothy, and Max.':
        photo = open('photos/mmvxyri1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, 'Неправильно, попробуй ещё раз!')
        bot.register_next_step_handler(message, oxf_ex1_num1)
    elif message.text.strip() == 'Главная 🏡':
        start(message)
    else:
        cat = open('photos/ty26hmpfe3f51.jpg', 'rb')
        bot.send_photo(message.chat.id, cat, 'Извини, я тебя не понял 😬')
        bot.register_next_step_handler(message, oxf_ex1_num1)
def oxf_ex1_num2(message):
    if message.text.strip() == 'Her friends, Steven and Sarah, were present at the party.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but_main = types.KeyboardButton("Главная 🏡")
        markup.add(but_main)
        photo = open('photos/christmas-dinner-a-family-preparing-christmas-dinner-and-looking-involved_259150-56199.jpg', 'rb')
        bot.send_message(message.chat.id, 'Awesome!')
        bot.send_photo(message.chat.id, photo, 'Задание №3\n'
                                               '\n'
                                               'My friend finds inspiration in cooking(,) her family(,) and her dog.', reply_markup=markup)
        bot.register_next_step_handler(message, oxf_ex1_num3)
    elif message.text.strip() == 'Her friends, Steven, and Sarah, were present at the party.':
        photo = open('photos/zato-ja-shablon.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, 'Неправильно, попробуй ещё раз!')
        bot.register_next_step_handler(message, oxf_ex1_num2)
    elif message.text.strip() == 'Главная 🏡':
        start(message)
    else:
        cat = open('photos/ty26hmpfe3f51.jpg', 'rb')
        bot.send_photo(message.chat.id, cat, 'Извини, я тебя не понял 😬')
        bot.register_next_step_handler(message, oxf_ex1_num2)
def oxf_ex1_num3(message):
    if message.text.strip() == 'My friend finds inspiration in cooking, her family, and her dog.':
        markup = types.InlineKeyboardMarkup()
        but_main = types.InlineKeyboardButton(text='<< Назад', callback_data='ford')
        markup.add(but_main)
        photo = open('photos/новый-молоток-желтый-шлем-стоковые-иллюстрации_csp6899697-transformed.jpg', 'rb')
        bot.send_message(message.chat.id, 'Good job!')
        bot.send_photo(message.chat.id, photo, 'Work in progress...', reply_markup=markup)
    elif message.text.strip() == 'My friend finds inspiration in cooking her family and her dog.':
        photo = open('photos/Halloween_vedma_21285.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, 'Неправильно, попробуй ещё раз!')
        bot.register_next_step_handler(message, oxf_ex1_num3)
    elif message.text.strip() == 'Главная 🏡':
        start(message)
    else:
        cat = open('photos/ty26hmpfe3f51.jpg', 'rb')
        bot.send_photo(message.chat.id, cat, 'Извини, я тебя не понял 😬')
        bot.register_next_step_handler(message, oxf_ex1_num3)

print('Working...')
bot.infinity_polling()