import requests
import os
from datetime import datetime
OBJETIVO = {
    "nombre": "fennec",
    "color": "black",
    "calcomania": "ombre"
}
WEBHOOK = os.getenv("WEBHOOK_URL")
URL_TIENDA = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
CABECERAS = {"User-Agent": "Mozilla/5.0"}
def revisar_tienda():
    if not WEBHOOK:
        print("Falta el secreto WEBHOOK_URL")
        return
    try:
        res = requests.get(URL_TIENDA, headers=CABECERAS, timeout=15)
        res.raise_for_status()
        items = res.json()["data"]["items"]
        print(f"Tienda cargada: {len(items)} objetos")
        for item in items:
            n = str(item.get("name","")).lower()
            c = str(item.get("paint","normal")).lower()
            d = str(item.get("decal","ninguna")).lower()
            if OBJETIVO["nombre"] in n and OBJETIVO["color"] in c and OBJETIVO["calcomania"] in d:
                aviso = "🚨 ¡SALIÓ LO QUE BUSCABAS!"\n"
                aviso += f"Objeto: {item.get('name')}\n"
                aviso += f"Color: {item.get('paint','Normal')}\n"
                aviso += f"Calcomanía: {item.get('decal','Ninguna')}"
                requests.post(WEBHOOK, json={"content": aviso})
                print("Aviso enviado!")
                return
        print("Todavía no está disponible")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    revisar_tienda()
