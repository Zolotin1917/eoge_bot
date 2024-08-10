import telebot
from telebot import types
token=('7431473620:AAGhcm3uWIrSlQfBX-OovOvBYE4W2dx23Jw')
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Висиит груша - нельзя скушать')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Груша")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):

    if message.text=="Лампа":
        bot.send_message(message.chat.id,'Верно!')
    else:
        bot.send_message(message.chat.id, 'Неверно!')
bot.infinity_polling()







