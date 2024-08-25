import telebot
from telebot import types
import sqlite3
import random
#import time

token = ('7431473620:AAF-YdmseUwhtN3jos7RUX6ppqn-XvgJUlg')
bot = telebot.TeleBot(token)
conn = sqlite3.connect('zagadki', check_same_thread=False)
cursor = conn.cursor()

connection = sqlite3.connect('Zagadki')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Zagadki')
zagadki = cursor.fetchall()

cursor.execute('SELECT text FROM Wrong_answer')
Wrong_answer = cursor.fetchall()

#connection = sqlite3.connect('Mat')
#cursor = connection.cursor()
cursor.execute('SELECT * FROM Mat')
Mat = cursor.fetchall()

cursor.execute('SELECT text FROM Otvetka')
Otvetka = cursor.fetchall()

#connection = sqlite3.connect('tem')
#cursor = connection.cursor()
#cursor.execute('SELECT * FROM tem')
#tem = cursor.fetchall()

#for oi in tem:
#  print(oi)

for text in Wrong_answer:
    print(text)

for text in Mat:
    print(text)

for text in Otvetka:
    print(text)

#users = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    global zagadka
    zagadka = zagadki[random.randint(0, len(zagadki)) - 1]
    print(zagadka)
    bot.send_message(message.chat.id, zagadka[1])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Новая загадка")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="", reply_markup=markup)


@bot.message_handler(regexp="Новая загадка")
def start_message(message):
    zagadka = zagadki[random.randint(0, len(zagadki)) - 1]
    print(zagadka)
    bot.send_message(message.chat.id, zagadka[1])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Новая загадка")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="", reply_markup=markup)

#@bot.message_handler(regexp="Связь/Поддержка")
#def start_message(message):
#    bot.send_message(message.chat.id, 'Связь, Поддержка и другое: @Zolotin1917')
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    btn1 = types.KeyboardButton("Связь/Поддержка")
#    markup.add(btn1)
#    bot.send_message(message.chat.id, text="", reply_markup=markup)


@bot.message_handler()
def message_reply(message):

    a = message.text.lower()
    #lst = [a]
    print('a= ', a)
    print('Ответ из бд:', zagadka[2].lower())
    print('Матные слова:', len(Mat))
    print('Ответки:', Otvetka)

    if a == zagadka[2].lower():
        bot.send_message(message.chat.id, 'Верно! Для того, чтобы перейти к следующей загадке напиши /start')
    elif a in list(Mat):
        print(len(a))
        print('Матное слово:', message.text.lower())
        a = Otvetka[random.randint(0, len(Otvetka)) - 1]
        print('Ответка:', a)
        bot.send_message(message.chat.id, a[0])
    else:
        print(a)
        wr = Wrong_answer[random.randint(0, len(Wrong_answer)) - 1]
        print(wr)
        bot.send_message(message.chat.id, wr[0])











bot.infinity_polling()
connection.close()
