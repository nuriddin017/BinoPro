import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL")  # Render URL'ni qo‘shasiz

url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
r = requests.post(url, data={"url": f"{APP_URL}/{TOKEN}"})
print("Webhook set result:", r.text)
