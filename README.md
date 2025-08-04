# Obra Nueva Buscador 🏡

Este proyecto es un bot automático que busca pisos en la costa de Galicia (desde Noia hasta Cambados) con las siguientes características:

- Obra nueva, promociones o reformas integrales recientes
- Terraza amplia (mínimo 12 m²)
- Vistas al mar o áticos con buena orientación
- Entrega de resultados diarios a través de Telegram
- Filtros de precio, habitaciones y estado de conservación
- Análisis de los anuncios con ayuda de IA (OpenAI)

## Archivos principales

- `main.py`: punto de entrada para ejecutar la búsqueda diaria
- `scraping.py`: lógica de scraping de los portales inmobiliarios
- `openai_analysis.py`: análisis inteligente del texto de los anuncios
- `telegram_send.py`: envía los resultados al bot de Telegram
- `config_local.json`: configuración privada (no se incluye en Git)
- `requirements.txt`: dependencias necesarias

## Cómo usar

1. Crea un archivo `config_local.json` con tus claves y filtros (ver `config_example.json` si está disponible).
2. Ejecuta el bot con: `python main.py`
3. Recibe las novedades directamente en tu bot de Telegram 🤖

## Repositorio mantenido por

**Angel FV** – afvafbsfb  
Licencia: uso personal

---
*Proyecto en desarrollo. Última actualización: Agosto 2025.*

## 🔐 Seguridad y configuración

- El archivo `config_local.json` contiene tus claves reales y **no debe subirse nunca** al repositorio. Ya está incluido en `.gitignore` por seguridad.
- En su lugar, se incluye un `config_example.json` como plantilla pública para facilitar la configuración sin exponer secretos.

