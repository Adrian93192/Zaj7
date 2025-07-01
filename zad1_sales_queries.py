import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# a) Sprzedaż tylko produktu „Laptop”
cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
print("Sprzedaż Laptopów:")
print(cursor.fetchall())

# b) Dane tylko z dni 2025-05-07 i 2025-05-08
cursor.execute("SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08')")
print("\nSprzedaż z 2025-05-07 i 2025-05-08:")
print(cursor.fetchall())

# c) Transakcje, w których cena jednostkowa > 200 zł
cursor.execute("SELECT * FROM sales WHERE unit_price > 200")
print("\nTransakcje z ceną jednostkową > 200 zł:")
print(cursor.fetchall())

# d) Łączna wartość sprzedaży dla każdego produktu
cursor.execute("SELECT product, SUM(quantity * unit_price) AS total_sales FROM sales GROUP BY product")
print("\nŁączna wartość sprzedaży dla każdego produktu:")
print(cursor.fetchall())

# e) Dzień z największą liczbą sprzedanych sztuk
cursor.execute("SELECT date, SUM(quantity) AS total_quantity FROM sales GROUP BY date ORDER BY total_quantity DESC LIMIT 1")
print("\nDzień z największą sprzedażą:")
print(cursor.fetchone())

conn.close()
