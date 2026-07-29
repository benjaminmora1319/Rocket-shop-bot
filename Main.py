import requests
import os

n = "fennec"
c = "black"
d = "ombre"
w = os.getenv("WEBHOOK_URL")
url = "https://api.tracker.gg/api/v2/rocket-league/standard/shop"
h = {"User-Agent":"Mozilla/5.0"}

def run():
    if not w:
        print("Falta el secreto WEBHOOK_URL")
        return
    try:
        r = requests.get(url, headers=h, timeout=10)
        r.raise_for_status()
        items = r.json()["data"]["items"]
        for i in items:
            nom = str(i.get("name","")).lower()
            col = str(i.get("paint","normal")).lower()
            dec = str(i.get("decal","ninguna")).lower()
            if n in nom and c in col and d in dec:
                m = "🚨 ENCONTRADO! " + str(i.get("name")) + " | " + str(i.get("paint")) + " | " + str(i.get("decal"))
                requests.post(w, json={"content": m})
                print("AVISO ENVIADO AL CANAL")
                return
        print("Todavia no esta disponible")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    run()

