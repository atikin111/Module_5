import os
import telebot
from telebot import types
from datetime import datetime
import json

TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TOKEN)

DREAM = "Сон"
WAKE = "Подъём"
DURATION = "Продолжительность сна"
QUALITY = "Оценка сна"
NOTES = "Заметки"

USER_DATA_BASE = 'DataBaseSleep_user.txt'

LIST_OF_CHOICES = [DREAM, WAKE, QUALITY, NOTES]

LIST_OF_QUALITY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

SLEEP_INFO_DICT = [
    {DREAM: [],
     WAKE: [],
     DURATION: [],
     QUALITY: [],
     NOTES: []}
    ]


def validate_message(message): # Функция проверки сообщения
    return message in LIST_OF_CHOICES

def open_file(name_file): # Функция открытия файла
    try:
        with open(name_file, encoding='utf-8') as f:
            user_database = json.load(f)
    except FileNotFoundError:
        user_database = {}
    return user_database

def save_database(user_id, sleep_indicator, user_time): # Сохранение данных в файл
    database = open_file(USER_DATA_BASE)
    if user_id in database:
        database[str(user_id)][-1][sleep_indicator] = user_time
    else:
        database[str(user_id)] = SLEEP_INFO_DICT
        database[str(user_id)][-1][sleep_indicator] = user_time
    with open(USER_DATA_BASE, 'w+', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=1)
        return database


def duration(user_id):
    user_data = open_file(USER_DATA_BASE)
    sleep_time = user_data[str(user_id)][-1][DREAM]
    wake_time = user_data[str(user_id)][-1][WAKE]
    duration_time = abs(sleep_time - wake_time)
    user_data[str(user_id)][-1][DURATION] = duration_time
    with open(USER_DATA_BASE, 'w+', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=1)
    return duration_time


# 1. Команда старт
@bot.message_handler(commands=['start'])
def start(message):
    start_text = (
        'Привет! Я буду помогать тебе отслеживать твой сон. '
        'Используй кнопки "Сон", "Подъем", "Оценка сна" и "Заметки".'
    )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*[types.KeyboardButton(name) for name in LIST_OF_CHOICES])
    bot.reply_to(message, start_text, reply_markup = markup)


# 2. Команда /sleep
@bot.message_handler(func = lambda message: message.text == DREAM)
def sleep(message):
    # Сообщение отправленное юзером
    user_message = str(message.text)
    # Проверка сообщения на соответствие
    right_message = validate_message(user_message)
    if not right_message:
        bot.send_message(message.chat.id, 'Выбери один из вариантов ответа ниже.')
    # Время отхода ко сну
    sleep_datatime = datetime.now()
    sleep_time = sleep_datatime.hour
    # Получаем id user'a
    user_id = message.from_user.id
    # Сохраняем новые данные:
    user_data = save_database(user_id, DREAM, sleep_time)
    bot.reply_to(message, f'Спокойной ночи! Не забудь сообщить мне, когда проснешься, '
                                      f'используя кнопку {WAKE}.')

# 3. Команда /wake
@bot.message_handler(func = lambda message: message.text == WAKE)
def wake(message):
    # Сообщение отправленное юзером
    user_message = str(message.text)
    # Проверка сообщения на соответствие
    right_message = validate_message(user_message)
    if not right_message:
        bot.send_message(message.chat.id, 'Выбери один из вариантов ответа ниже.')
    # Время подъема
    wake_datatime = datetime.now()
    wake_time = wake_datatime.hour
    # Получаем id user'a
    user_id = message.from_user.id
    # Получаем данные с файла
    user_data = save_database(user_id, WAKE, wake_time)
    duration_time = duration(user_id)
    bot.reply_to(message, f'Доброе утро! Хорошего тебе дня! Ты проспал около {duration_time} часов. Не забудь оценить качество '
                          f'сна кнопкой "Оценка сна" и оставить заметки с помощью кнопки "Заметки".')


# 4. Команда /quality
@bot.message_handler(func = lambda message: message.text == QUALITY)
def quality(message):
    # Сообщение отправленное юзером
    user_message = str(message.text)
    # Проверка сообщения на соответствие
    right_message = validate_message(user_message)
    if not right_message:
        bot.send_message(message.chat.id, 'Выбери один из вариантов ответа ниже.')
    bot.reply_to(message, 'Оцени качество своего сна от 1 до 10!')

# 5. Декоратор для обработки интовых значений
@bot.message_handler(func = lambda m: m.text.isdigit())
def message_digital(message):
    user_id = message.from_user.id
    user_message = int(message.text)
    user_data = open_file(USER_DATA_BASE)
    if user_message in LIST_OF_QUALITY:
        user_data[str(user_id)][-1][QUALITY] = user_message
        with open(USER_DATA_BASE, 'w+', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=1)
        bot.reply_to(message, 'Спасибо, оценка сохранена! Оставь заметку о своем сне :)')
    else:
        bot.send_message(message.chat.id, 'Оцени качество своего сна! Введи значение от 1 до 10!')


# 6. Декоратор для команды /notes
@bot.message_handler(func = lambda message: message.text == NOTES)
def notes(message):
    # Сообщение отправленное юзером
    user_message = str(message.text)
    # Проверка сообщения на соответствие
    right_message = validate_message(user_message)
    if not right_message:
        bot.send_message(message.chat.id, 'Выбери один из вариантов ответа ниже')
    bot.reply_to(message, 'Оставь заметку о своем сне :) Как тебе спалось?')


# 7. Декоратор для обработки текстовых сообщений
@bot.message_handler(func = lambda message: message.text)
def message_text(message):
    user_id = message.from_user.id
    user_message = message.text
    user_data = open_file(USER_DATA_BASE)
    user_data[str(user_id)][-1][NOTES] = user_message
    with open(USER_DATA_BASE, 'w+', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=1)
    bot.reply_to(message, 'Спасибо, заметка сохранена! Не забудь отметиться, когда снова будешь ложиться спать!')


bot.polling(none_stop = True, interval = 0)

# Попробовать облегчить код и сгруппировать все через функции.