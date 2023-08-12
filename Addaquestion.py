import telebot


bot = telebot.TeleBot("6287653143:AAGim4qWjPPoTb2HXMm0WkPVBtfNNHDjg2E")

@bot.message_handler(func=lambda message: True)
def add_question_text(message):
    
        new_text = "اضف اذكار - " + message.text
        bot.send_message(message.chat.id, new_text)


bot.infinity_polling()