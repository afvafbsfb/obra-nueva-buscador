
import requests

telegram_token = "8498146268:AAGNDB3TOjaalg2jgbzz-NS1R7j98SmEZD0"

url = f"https://api.telegram.org/bot{telegram_token}/getUpdates"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data["result"]:
        for update in data["result"]:
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                user = update["message"]["chat"].get("first_name", "Sin nombre")
                print(f"✅ chat_id encontrado: {chat_id} (usuario: {user})")
    else:
        print("⚠️ No se han recibido mensajes aún. Escribe al bot primero.")
else:
    print("❌ Error al conectar con Telegram")
