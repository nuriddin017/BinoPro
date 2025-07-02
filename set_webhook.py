import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL")  # Render dan olgan URL, masalan: https://telegram-webhook-bot.onrender.com

webhook_url = f"{APP_URL}/webhook"  # Faqat /webhook route

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    data={"url": webhook_url}
)

print("Webhook set result:", response.text)
