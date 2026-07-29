import requests
import os

n = "fennec"
c = "black"
w = os.getenv("WEBHOOK_URL")
url = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
h = {"User-Agent":"Mozilla/5.0"}

def revisar():
    if not w:
        print("Falta el secreto")
        return
    try:
        r = requests.get(url, headers=h, timeout=10)
        r.raise_for_status()
        items = r.json()["data"]["items"]
        for i in items:
            nom = str(i.get("name","")).lower()
            col = str(i.get("paint","normal")).lower()
            if n in nom and c in col:
                m = "🚨 ¡SALIÓ LO QUE BUSCABAS!\n"
                m += "Objeto: " + str(i.get("name")) + "\n"
                m += "Color: " + str(i.get("paint","Normal"))
                requests.post(w, json={"content": m})
                print("AVISO ENVIADO")
                return
        print("Todavía no está disponible")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    revisar()
