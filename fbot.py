import settings
import telebot

bot = telebot.TeleBot(settings.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcom(message):
    bot.reply_to(message, "Hello friend!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Help your self')

@bot.message_handler(commands=['kurs'])
def send_kurs(message):
    kurs=0
    text = message.text
    currency = text[4,]
    bot.send_message(message.chat.id, currency)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
