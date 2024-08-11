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
wrong_answer = cursor.fetchall()




for text in wrong_answer:
    print(text)




@bot.message_handler(commands=['start'])
def start_message(message):
    global zagadka
    zagadka = zagadki[random.randint(0, len(zagadki)) - 1]
    print(zagadka)
    bot.send_message(message.chat.id,zagadka[1])



@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler()
def message_reply(message):
    a = message.text.lower()
    print( 'a= ', a)
    print('Ответ из бд:', zagadka[2].lower())
    if a == zagadka[2].lower():
        bot.send_message(message.chat.id,'Верно!')
    else:


        Wrong_answer = text[random.randint(0, len(Wrong_answer)) - 1]
        print(text)
        bot.send_message(message.chat.id, text[2])

    bot.polling(none_stop=True)

bot.infinity_polling()
connection.close()








