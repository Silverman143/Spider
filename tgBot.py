import telebot

bot = telebot.TeleBot("1874521875:AAE1yavVTI15paSQ5mKka_Nt3Eqs9b6pf2k")
ownerChat = 522757046

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     print(message.chat.id)
# 	# bot.reply_to(message, "Howdy, how are you doing?")
#
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# bot.infinity_polling()

def SendData(data):
    bot.send_message(ownerChat, data)
