import requests
import time
import csv
import datetime

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"

headers = {
    "x-cg-api-key": "SUA_API_KEY_AQUI"  
}

start = int(time.mktime(time.strptime("2024-03-01", "%Y-%m-%d")))
end = int(time.mktime(time.strptime("2024-12-31", "%Y-%m-%d")))

params = {
    "vs_currency": "usd",
    "from": start,
    "to": end
}

response = requests.get(url, headers=headers, params=params)

# 200 indica se o request deu tudo certo 
if response.status_code == 200: 
    data = response.json()
    
    daily_data = {}

    for price_data in data["prices"]:
        timestamp = price_data[0] // 1000  
        date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        price = price_data[1]

        if date not in daily_data:
            daily_data[date] = {"open": price, "high": price, "low": price, "close": price}
        else:
            daily_data[date]["high"] = max(daily_data[date]["high"], price)
            daily_data[date]["low"] = min(daily_data[date]["low"], price)
            daily_data[date]["close"] = price  

  
    market_caps = {datetime.datetime.utcfromtimestamp(mc[0] // 1000).strftime('%Y-%m-%d'): mc[1] for mc in data["market_caps"]}
    volumes = {datetime.datetime.utcfromtimestamp(v[0] // 1000).strftime('%Y-%m-%d'): v[1] for v in data["total_volumes"]}

    # Criar um arquivo CSV
    with open("dados6meses.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Open", "High", "Low", "Close", "Market Cap", "Volume"])

        # Escrever os dados diários no CSV
        for date, values in sorted(daily_data.items()):
            market_cap = market_caps.get(date, "N/A")
            volume = volumes.get(date, "N/A")
            writer.writerow([date, values["open"], values["high"], values["low"], values["close"], market_cap, volume])
    
   