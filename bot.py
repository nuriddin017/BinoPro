import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")  # ✔️ environment variable orqali token olish
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Webhook endpoint – token emas, oddiy so‘z bilan
@app.route('/webhook', methods=['POST'])  # ✔️ xavfsizroq
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# /start komandasi
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Men webhook orqali ishlayapman!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
