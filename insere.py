import sqlite3
import csv

banco = r'C:\Users\migue\Documents\cryptodb\requisicoes\cryptodb'
dados_csv = r'C:\Users\migue\Documents\cryptodb\requisicoes\dados6meses.csv'  


conector = sqlite3.connect(banco)
cursor = conector.cursor()

cursor.execute("INSERT OR IGNORE INTO ticker (id_ticker, ticker) VALUES (1, 'BTC-USD')")
cursor.execute("INSERT OR IGNORE INTO ds_coin (id_ticker, coin_name) VALUES (1, 'Bitcoin')")
conector.commit()


with open(dados_csv, newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  
    
    for linha in leitor:
        date, open_, high, low, close, market_camp, volume = linha
        cursor.execute("""
            INSERT OR REPLACE INTO price (id_ticker, date, open, close, market_camp, high, low, volume)
            VALUES (1, ?, ?, ?, ?, ?, ?, ?)
        """, (date, open_, close, market_camp, high, low, volume))


conector.commit()
cursor.close()
conector.close()

