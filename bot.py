import telebot
import os
from flask import Flask, request, jsonify

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Root route qo'shish (404 xatolikni hal qilish uchun)
@app.route('/')
def home():
    return jsonify({
        "status": "Bot is running",
        "webhook": "active"
    })

# Health check
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    except Exception as e:
        print(f"Webhook error: {e}")
        return jsonify({"error": str(e)}), 500

# /start komandasi
@bot.message_handler(commands=['start'])
def start_handler(message):
    welcome_text = """
🎉 Assalomu alaykum!

Men webhook orqali ishlayapman va to'liq faolman!

📋 Mavjud buyruqlar:
/start - Botni ishga tushirish
/help - Yordam
/info - Bot haqida ma'lumot
    """
    bot.send_message(message.chat.id, welcome_text)

# /help komandasi
@bot.message_handler(commands=['help'])
def help_handler(message):
    help_text = """
📋 Yordam

Mavjud buyruqlar:
/start - Botni qayta ishga tushirish
/help - Bu yordam xabari
/info - Bot haqida ma'lumot

❓ Qo'shimcha savollar bo'lsa, admin bilan bog'laning.
    """
    bot.send_message(message.chat.id, help_text)

# /info komandasi
@bot.message_handler(commands=['info'])
def info_handler(message):
    info_text = """
ℹ️ Bot haqida ma'lumot

🔧 Texnik xususiyatlar:
• Webhook rejimida ishlamoqda
• Flask server orqali deploy qilingan
• Render platformasida joylashgan

📊 Status: Faol
🕐 Ishlash vaqti: 24/7
    """
    bot.send_message(message.chat.id, info_text)

# Barcha boshqa xabarlar uchun
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = f"Siz yozdingiz: {message.text}\n\nBuyruqlar ro'yxati uchun /help yuboring."
    bot.send_message(message.chat.id, response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting bot on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)