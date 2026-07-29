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
                m = "SALIO FENNEC BLACK! " + str(i.get("name")) + " " + str(i.get("paint"))
                requests.post(w, json={"content": m})
                print("AVISO ENVIADO")
                return
        print("No esta aun")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    revisar()
