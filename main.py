import requests
import os

busco_nombre = "fennec"
busco_color = "black"
busco_calco = "ombre"

webhook = os.getenv("WEBHOOK_URL")
url_api = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
cabeceras = {"User-Agent": "Mozilla/5.0"}

def main():
    if not webhook:
        print("Falta el secreto WEBHOOK_URL")
        return
    try:
        respuesta = requests.get(url_api, headers=cabeceras, timeout=15)
        respuesta.raise_for_status()
        datos = respuesta.json()["data"]["items"]
        print(f"Cargados {len(datos)} objetos")
        for item in datos:
            nom = str(item.get("name","")).lower()
            col = str(item.get("paint","normal")).lower()
            cal = str(item.get("decal","ninguna")).lower()
            if busco_nombre in nom and busco_color in col and busco_calco in cal:
                mensaje = "ENCONTRADO! Item: " + str(item.get("name")) + " | Color: " + str(item.get("paint","Normal")) + " | Calcomania: " + str(item.get("decal","Ninguna"))
                requests.post(webhook, json={"content": mensaje})
                print("AVISO ENVIADO")
                return
        print("No disponible aun")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

