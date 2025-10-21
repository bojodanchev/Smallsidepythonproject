import requests
import pandas as pd
from datetime import datetime
API_URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
def fetch_prices():
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    data = response.json()
    timestamp = datetime.utcnow().isoformat()
    rows = []
    for coin, info in data.items():
        rows.append({"asset": coin, "usd_price": info["usd"], "timestamp": timestamp})
    return pd.DataFrame(rows)
def main():
    df = fetch_prices()
    df.to_csv("data.csv", index=False)
    print(df)
if __name__ == "__main__":
    main()
