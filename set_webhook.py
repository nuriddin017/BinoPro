import requests
import os
from dotenv import load_dotenv

# .env faylini yuklash (local test uchun)
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL", "https://binopro.onrender.com")  # Sizning actual URL

# Webhook URL to'g'ri formatda
webhook_url = f"{APP_URL}/webhook"

print(f"Setting webhook to: {webhook_url}")

# Webhook o'rnatish
response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    data={"url": webhook_url}
)

result = response.json()
print("Webhook set result:", result)

if result.get('ok'):
    print("✅ Webhook muvaffaqiyatli o'rnatildi!")
else:
    print("❌ Webhook o'rnatishda xatolik:", result.get('description'))

# Webhook holatini tekshirish
check_response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo")
webhook_info = check_response.json()

if webhook_info.get('ok'):
    info = webhook_info['result']
    print("\n📊 Webhook holati:")
    print(f"URL: {info.get('url', 'Not set')}")
    print(f"Pending updates: {info.get('pending_update_count', 0)}")
    if info.get('last_error_message'):
        print(f"Last error: {info['last_error_message']}")
        print(f"Error date: {info.get('last_error_date', 'Unknown')}")
    else:
        print("✅ Xatoliklar yo'q")