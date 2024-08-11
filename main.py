import telebot
from telebot import types
import sqlite3
import random


token=('7431473620:AAGhcm3uWIrSlQfBX-OovOvBYE4W2dx23Jw')
bot=telebot.TeleBot(token)
conn = sqlite3.connect('zagadki', check_same_thread=False)
cursor = conn.cursor()

connection = sqlite3.connect('zagadki')
cursor = connection.cursor()
cursor.execute('SELECT * FROM zagadki')
zagadki = cursor.fetchall()


#for zagadka in zagadki:
 # print(zagadka)


zagadka = zagadki[random.randint(0, len(zagadki))-1]
print(zagadka)

@bot.message_handler(commands=['start'])
def start_message(message):
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
    print(a)
    print(zagadka[2].text.lower())
    if a == zagadka[2].text.lower():
        bot.send_message(message.chat.id,'Верно!')
    else:
        bot.send_message(message.chat.id, 'Неверно!')



        bot.polling(none_stop=True)

bot.infinity_polling()
connection.close()








