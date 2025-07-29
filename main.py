
from scraping import obtener_anuncios
from openai_analysis import analizar_anuncio
from telegram_send import enviar_a_telegram
import json
import csv
import os

# Cargar configuración de forma segura
config_path = "config_local.json" if os.path.exists("config_local.json") else "config.json"
with open(config_path, "r") as f:
    config = json.load(f)

def guardar_csv(datos):
    with open("resultados.csv", "w", newline='', encoding="utf-8") as csvfile:
        campos = ["titulo", "precio", "terraza", "vistas_mar", "orientacion", "url"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for dato in datos:
            writer.writerow(dato)

def main():
    print("🔍 Buscando anuncios...")
    anuncios = obtener_anuncios(config)

    print("🤖 Analizando con ChatGPT...")
    resultados = [analizar_anuncio(anuncio, config["openai_api_key"]) for anuncio in anuncios]

    mensaje = f"📆 Informe de obra nueva

"
    for r in resultados:
        mensaje += (
            f"🏠 <b>{r['titulo']}</b>
"
            f"• Precio: {r['precio']}
"
            f"• Terraza: {r['terraza']} (comer fuera: {'✅' if r['terraza_util'] else '❌'})
"
            f"• Vistas al mar: {'✅' if r['vistas_mar'] else '❌'}
"
            f"• Orientación: {r['orientacion'] or 'No especificada'}
"
            f"🔗 {r['url']}

"
        )

    enviar_a_telegram(mensaje, config)

    if config.get("guardar_csv", False):
        guardar_csv(resultados)

if __name__ == "__main__":
    main()
