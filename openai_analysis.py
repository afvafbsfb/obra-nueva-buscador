import openai

def analizar_anuncio(anuncio, api_key):
    openai.api_key = api_key
    prompt = (
        f"Analiza el siguiente anuncio de apartamento y responde:
"
        f"1. ¿Tiene vistas al mar? (sí/no)
"
        f"2. ¿La terraza permite comer fuera? (sí/no)
"
        f"3. ¿Qué orientación tiene (si se menciona)?

"
        f"Anuncio: {anuncio['descripcion']}"
    )

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=150
        )
        texto = respuesta['choices'][0]['message']['content'].lower()
        return {
            "titulo": anuncio["titulo"],
            "precio": anuncio["precio"],
            "terraza": "sí" if "terraza" in anuncio["descripcion"].lower() else "no",
            "terraza_util": "sí" in texto and "comer" in texto,
            "vistas_mar": "sí" in texto and "mar" in texto,
            "orientacion": (
                "sur" if "sur" in texto else
                "este" if "este" in texto else
                "oeste" if "oeste" in texto else
                "norte" if "norte" in texto else None
            ),
            "url": anuncio["url"]
        }
    except Exception as e:
        print(f"Error con OpenAI: {e}")
        return {**anuncio, "terraza_util": False, "vistas_mar": False, "orientacion": None}
