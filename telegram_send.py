import requests

def enviar_a_telegram(mensaje, config):
    url = f"https://api.telegram.org/bot{config['telegram_token']}/sendMessage"
    payload = {
        "chat_id": config["telegram_chat_id"],
        "text": mensaje,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error enviando mensaje a Telegram: {e}")
