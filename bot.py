import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("7782911772:AAHfg2jrQWcv59FfdREHeSw3y77drULasdw")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Telegramdan kelgan so‘rovni qabul qilish
@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Oddiy start komandasi
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Men webhook orqali ishlayapman!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
