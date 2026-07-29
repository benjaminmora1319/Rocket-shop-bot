import requests
import os
from datetime import datetime

busco_nombre = "fennec"
busco_color = "black"
busco_calco = "ombre"

webhook = os.getenv("WEBHOOK_URL")
url = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
cabecera = {"User-Agent": "Mozilla/5.0"}

def chequear():
    if not webhook:
        print("Falta el secreto")
        return
    try:
        r = requests.get(url, headers=cabecera, timeout=15)
        r.raise_for_status()
        lista = r.json()["data"]["items"]
        print(f"Hay {len(lista)} items")
        for i in lista:
            nom = str(i.get("name","")).lower()
            col = str(i.get("paint","normal")).lower()
            cal = str(i.get("decal","ninguna")).lower()
            if busco_nombre in nom and busco_color in col and busco_calco in cal:
                msg = "ENCONTRADO!\n"
                msg = msg + "Item: " + str(i.get("name")) + "\n"
                msg = msg + "Color: " + str(i.get("paint","Normal")) + "\n"
                msg = msg + "Calcomania: " + str(i.get("decal","Ninguna"))
                requests.post(webhook, json={"content": msg})
                print("MENSAJE ENVIADO")
                return
        print("No esta aun")
    except Exception as err:
        print(f"ERROR: {err}")

if __name__ == "__main__":
    chequear()
