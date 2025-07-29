import requests
from bs4 import BeautifulSoup

# Simula scraping en varios portales (versión básica y legal con URLs de búsqueda)
def obtener_anuncios(config):
    portales = [
        {
            "nombre": "Idealista (Cambados)",
            "url": "https://www.idealista.com/venta-obranueva/cambados-pontevedra/"
        },
        {
            "nombre": "Idealista (A Pobra)",
            "url": "https://www.idealista.com/venta-obranueva/a-pobra-do-caraminal-a-coruna/"
        },
        {
            "nombre": "Pisos.com",
            "url": "https://www.pisos.com/venta/pisos-a_pobra_do_caraminal/con-terraza/"
        },
        {
            "nombre": "Fotocasa",
            "url": "https://www.fotocasa.es/es/comprar/viviendas/a-pobra-do-caraminal/todas-las-zonas/con-terraza/obra-nueva/"
        },
        {
            "nombre": "Trovit",
            "url": "https://casas.trovit.es/index.php/cod.search_homes/type.1/what_d.pobra+do+caramiñal+cambados/ord.price/"
        },
        {
            "nombre": "Yaencontre",
            "url": "https://www.yaencontre.com/venta/pisos/a-pobra-do-caraminal/t-aticos/f-terraza"
        }
    ]

    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []

    for portal in portales:
        try:
            r = requests.get(portal["url"], headers=headers, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            texto = soup.get_text().lower()

            # Extraer títulos y párrafos
            posibles = soup.find_all(['h2', 'h3', 'p', 'a'])
            for elemento in posibles:
                desc = elemento.get_text(strip=True).lower()
                if any(k in desc for k in ['terraza', 'ático', 'obra nueva', 'vistas al mar']):
                    resultados.append({
                        "titulo": f"{portal['nombre']}",
                        "precio": "Consultar portal",
                        "descripcion": desc,
                        "url": portal["url"]
                    })
        except Exception as e:
            print(f"Error en {portal['nombre']}: {e}")

    return resultados
