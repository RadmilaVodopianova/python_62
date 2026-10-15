import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   category TEXT,
   price REAL,
   quantity INTEGER
)
""")

cursor.execute("DELETE FROM products")

products = [
    ("Laptop", "Electronics", 25000, 5),
    ("Mouse", "Electronics", 500, 20),
    ("Keyboard", "Electronics", 1200, 10),
    ("Monitor", "Electronics", 7000, 7),
    ("Desk", "Furniture", 4500, 3),
    ("Chair", "Furniture", 3000, 8),
    ("Notebook", "Stationery", 80, 50),
    ("Pen", "Stationery", 25, 100),
    ("Headphones", "Electronics", 2200, 0),
    ("Lamp", "Furniture", 900, 12)
]

cursor.executemany("""
INSERT INTO products (name, category, price, quantity)
VALUES (?, ?, ?, ?)
""", products)

conn.commit()
conn.close()


