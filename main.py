import requests
import os
from datetime import datetime

# 🎯 Objetos a vigilar
OBJETIVO = {
    "nombre": "fennec",
    "color": "black",
    "calcomania": "ombre"
}

# Obtiene el enlace de forma segura desde el secreto que creaste
WEBHOOK = os.getenv("WEBHOOK_URL")

# Configuración de la tienda
URL_TIENDA = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
CABECERAS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

def revisar_tienda():
    if not WEBHOOK:
        print("❌ FALTA CONFIGURAR EL ENLACE EN SECRETS")
        return

    try:
        # Pedimos los datos de la tienda
        respuesta = requests.get(URL_TIENDA, headers=CABECERAS, timeout=15)
        respuesta.raise_for_status()
        datos = respuesta.json()
        lista_items = datos.get("data", {}).get("items", [])
        print(f"✅ Tienda cargada: {len(lista_items)} objetos")

        # Buscamos lo que queremos
        for item in lista_items:
            nombre = str(item.get("name", "")).lower()
            color = str(item.get("paint", "normal")).lower()
            calco = str(item.get("decal", "ninguna")).lower()

            if (OBJETIVO["nombre"] in nombre and
                OBJETIVO["color"] in color and
                OBJETIVO["calcomania"] in calco):

                # Armamos el aviso
                aviso = (
                    "🚨 ¡SALIÓ LO QUE BUSCABAS!\n"
                    f"📦 Objeto: {item.get('name')}\n"
                    f"🎨 Color: {item.get('paint', 'Normal')}\n"
                    f"✨ Calcomanía: {item.get('decal', 'Ninguna')}\n"
                    f"🕒 Hora: {datetime.now().strftime('%H:%M')}"
                )
                # Enviamos el mensaje
                requests.post(WEBHOOK, json={"content": aviso})
                print("✅ AVISO ENVIADO AL SERVIDOR")
                return

        print("🔎 No está disponible todavía, seguimos vigilando...")

    except Exception as error:
        print(f"❌ ERROR: {str(error)}")

if __name__ == "__main__":
    revisar_tienda()
