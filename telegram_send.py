import json
import requests
import sys

# Cargar config
with open("config_local.json", encoding="utf-8") as f:
    config = json.load(f)

# Leer mensaje desde argumentos
if len(sys.argv) < 2:
    print("❌ Uso: python telegram_send.py \"mensaje a enviar\"")
    sys.exit(1)

mensaje = sys.argv[1]
chat_id = config["telegram_chat_id"]
token = config["telegram_token"]

# Enviar a Telegram
url = f"https://api.telegram.org/bot{token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": mensaje,
    "parse_mode": "Markdown"
}

response = requests.post(url, data=payload)

# Mostrar resultado
if response.status_code != 200:
    print("❌ Error al enviar:", response.status_code, response.text)
else:
    print("✅ Mensaje enviado correctamente.")