import sqlite3

conector = sqlite3.connect(r'C:\Users\migue\Documents\cryptodb\requisicoes\cryptodb')
cursor = conector.cursor()

cursor.execute("""
    CREATE TABLE ticker (
        id_ticker INTEGER PRIMARY KEY,
        ticker TEXT NOT NULL,
    )
""")

cursor.execute("""
    CREATE TABLE price (
        id_ticker INTEGER NOT NULL,
        date TEXT NOT NULL,
        open DECIMAL,
        close DECIMAL,
        market_camp FLOAT,
        high DECIMAL,
        low DECIMAL,
        volume DECIMAL,
        PRIMARY KEY (id_ticker, date),
        FOREIGN KEY (id_ticker) REFERENCES ticker (id_ticker)
    )
""")

cursor.execute("""
    CREATE TABLE ds_coin (
        id_ticker INTEGER PRIMARY KEY,
        coin_name TEXT NOT NULL,
        FOREIGN KEY (id_ticker) REFERENCES ticker (id_ticker)
    )
""")


conector.commit()
cursor.close()
conector.close()
