import telebot
from telebot import types
token='7505580331:AAF07RzwYW_tcqKIYq_8JmlobxHAsD6iyhs'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'xxx')
@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("xxxx")
	markup.add(item1)																																					