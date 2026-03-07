import sqlite3

conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS stocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sym TEXT NOT NULL,
        name TEXT NOT NULL,
        price REAL,
        chg REAL,
        pe REAL,
        div REAL,
        beta REAL,
        sector TEXT,
        mktcap TEXT,
        momentum TEXT,
        debt TEXT
    )
''')

stocks = [
    ('EQTY', 'Equity Group Holdings', 77.25, 0.98, 8.0, 4.25, 1.1, 'Banking', 'Large', 'Strong', 'low'),
    ('KCB', 'Kenya Commercial Bank', 80.25, 4.22, 6.78, 4.00, 1.2, 'Banking', 'Large', 'Moderate', 'medium'),
    ('SCOM', 'Safaricom PLC', 32.40, -2.14, 14.90, 1.50, 0.8, 'Telecoms', 'Large', 'Strong', 'low'),
    ('EABL', 'East African Breweries', 259.50, 1.67, 15.0, 9.50, 1.0, 'Manufacturing', 'Large', 'Weak', 'high'),
    ('KPLC', 'Kenya Power & Lighting Co', 18.50, 0.54, 10.0, 1.10, 0.8, 'Energy', 'Medium', 'Strong', 'medium'),
    ('BAT', 'British American Tobacco', 567.00, 5.39, 20.0, 70.00, 0.7, 'Manufacturing', 'Large', 'Moderate', 'low'),
    ('KQ', 'Kenya Airways', 5.60, -0.36, 4.0, 0.0, 1.8, 'Transport', 'Small', 'Weak', 'high'),
    ('JUB', 'Jubilee Holdings', 374.60, 0.34, 12.0, 13.50, 0.9, 'Insurance', 'Medium', 'Moderate', 'low'),
    ('DTK', 'Diamond Trust Bank', 154.75, -2.21, 7.5, 7.00, 1.2, 'Banking', 'Medium', 'Strong', 'medium'),
    ('NBV', 'Nairobi Business Ventures', 1.48, -3.90, 5.0, 0.0, 1.5, 'Investment', 'Small', 'Weak', 'high'),
    ('SBIC', 'Stanbic Holdings', 256.50, 0.49, 9.0, 45.00, 1.0, 'Banking', 'Large', 'Strong', 'low'),
    ('KNRE', 'Kenya Reinsurance', 3.98, -1.01, 6.0, 0.15, 1.3, 'Insurance', 'Medium', 'Moderate', 'medium'),
]

cursor.executemany('''
    INSERT INTO stocks (sym, name, price, chg, pe, div, beta, sector, mktcap, momentum, debt)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', stocks)

conn.commit()
conn.close()

print("Database created and stocks inserted successfully!")