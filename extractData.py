import requests
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()
url: str = os.getenv("API_URL")
key: dict = {"key": os.getenv("API_KEY")}

r = []

with requests.Session() as session:
    for i in range(20):
        try:
            response = session.get(url, params=key, timeout=5).json()
            r.append(response)
            print(f"Request ke-{i+1}: Data {response['source_ip']}")

        except requests.exceptions.RequestException as e:
            print(f"Request ke-{i+1} Gagal: {e}")

        time.sleep(1)

if os.path.exists("network_log.json"):
    with open("network_log.json", "a", encoding="utf-8") as file:
        file.write(json.dumps(r, indent=4))
else:
    with open("network_log.json", "w", encoding="utf-8") as file:
        json.dump(r, file, indent=4)
