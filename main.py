import telebot
from telebot import types
import sqlite3
import random


token=('7431473620:AAGhcm3uWIrSlQfBX-OovOvBYE4W2dx23Jw')
bot=telebot.TeleBot(token)
conn = sqlite3.connect('zagadki', check_same_thread=False)
cursor = conn.cursor()

connection = sqlite3.connect('Zagadki')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Zagadki')
zagadki = cursor.fetchall()

cursor.execute('SELECT text FROM Wrong_answer')
Wrong_answer = cursor.fetchall()

cursor.execute('SELECT matnye_slova FROM mat')
mat = cursor.fetchall()

cursor.execute('SELECT moshnaya_otvetka FROM otvetka')
otvetka = cursor.fetchall()


for text in Wrong_answer:
    print(text)

for matnye_slova in mat:
    print(matnye_slova)

for moshnaya_otvetka in otvetka:
    print(moshnaya_otvetka)


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




@bot.message_handler()
def message_reply(message):
    a = message.text.lower()
    print( 'a= ', a)
    print('Ответ из бд:', zagadka[2].lower())
    if a == zagadka[2].lower():
        bot.send_message(message.chat.id,'Верно! Для того, чтобы перейти к следующей загадке напиши /start')
    elif a == matnye_slova[1].lower():
        mo = moshnaya_otvetka[random.randint(0, len(moshnaya_otvetka)) - 1]
        print(mo)
        bot.send_message(message.shat.id, mo[1])
    else:
        wr = Wrong_answer[random.randint(0, len(Wrong_answer)) - 1]
        print(wr)
        bot.send_message(message.chat.id, wr[0])






bot.infinity_polling()
connection.close()









