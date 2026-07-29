import requests
import time
from datetime import datetime

# Configuración del bot
WEBHOOK_URL = "TU_URL_DE_WEBHOOK_AQUI"  # Reemplaza con tu URL de webhook (Discord, Telegram, etc.)
TIENDA_API = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
OBJETOS_A_VIGILAR = [
    {"nombre": "Fennec", "color": "Black", "calcomania": "Ombre"}
]
CHECK_INTERVAL = 60  # Revisa la tienda cada 60 segundos (1 minuto)

def revisar_tienda():
    try:
        response = requests.get(TIENDA_API)
        response.raise_for_status()
        datos_tienda = response.json()

        items_disponibles = datos_tienda.get("data", {}).get("items", [])
        items_nuevos = []

        for item in items_disponibles:
            nombre_item = item.get("name", "").strip()
            color_item = item.get("color", "").strip()
            calcomania_item = item.get("decals", [{}])[0].get("name", "").strip()

            # Verifica si el item coincide con alguno de la lista
            for objeto in OBJETOS_A_VIGILAR:
                if (objeto["nombre"].lower() in nombre_item.lower() and
                    objeto["color"].lower() in color_item.lower() and
                    objeto["calcomania"].lower() in calcomania_item.lower()):

                    mensaje = (
                        f"¡ALERTA! Nuevo objeto en la tienda:\n"
                        f"**{nombre_item}** ({color_item})\n"
                        f"Calcomanía: **{calcomania_item}**\n"
                        f"Hora: {datetime.now().strftime('%H:%M:%S')}"
                    )
                    items_nuevos.append(mensaje)

        if items_nuevos:
            enviar_alerta("\n
".join(items_nuevos))

    except Exception as e:
        print(f"Error al revisar la tienda: {e}")

def enviar_alerta(mensaje):
    """Envía el mensaje al webhook configurado."""
    try:
        # Ajusta el payload según el servicio de webhook que uses (Discord, Telegram, etc.)
        # Ejemplo para Discord:
        payload = {"content": mensaje}
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Alerta enviada con éxito!")
    except Exception as e:
        print(f"Error al enviar la alerta: {e}")

if __name__ == "__main__":
    print("Bot de vigilancia de tienda iniciado...")
    print(f"Revisando cada {CHECK_INTERVAL} segundos.")
    print(f"Objetos a vigilar: {[obj['nombre'] + ' ' + obj['color'] for obj in OBJETOS_A_VIGILAR]}")

    while True:
        revisar_tienda()
        time.sleep(CHECK_INTERVAL)

