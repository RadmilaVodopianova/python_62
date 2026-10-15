
import sqlite3

conn = sqlite3.connect("Sales.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Salesmen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salesman_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    sale_date TEXT,
    FOREIGN KEY (salesman_id) REFERENCES Salesmen(id),
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
)
""")

cursor.execute("DELETE FROM Sales")
cursor.execute("DELETE FROM Salesmen")
cursor.execute("DELETE FROM Customers")

salesmen = [
    (1, "Bib", "Kyiv"),
    (2, "Bob", "Odesa"),
    (3, "Bill", "Lviv")
]

cursor.executemany("""
INSERT INTO Salesmen (id, name, city)
VALUES (?, ?, ?)
""", salesmen)

customers = [
    (1, "Bible", "Kyiv"),
    (2, "Anna", "Odesa"),
    (3, "Maria", "Kharkiv"),
    (4, "Sofia", "Lviv")
]

cursor.executemany("""
INSERT INTO Customers (id, name, city)
VALUES (?, ?, ?)
""", customers)

sales = [
    (1, 1, 1200, "2026-10-01"),
    (1, 2, 2500, "2026-10-02"),
    (2, 1, 1800, "2026-10-03"),
    (2, 3, 900, "2026-10-04"),
    (3, 4, 3200, "2026-10-05"),
    (3, 2, 1500, "2026-10-06"),
    (1, 4, 700, "2026-10-07")
]

cursor.executemany("""
INSERT INTO Sales (salesman_id, customer_id, amount, sale_date)
VALUES (?, ?, ?, ?)
""", sales)

conn.commit()

print("Базу даних Sales створено успішно!")


def show_query(number, title, query, params=()):
    print(f"\n{number}. {title}")
    cursor.execute(query, params)

    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("Даних немає")


show_query(1, "Усі угоди", """
SELECT Sales.id, Salesmen.name, Customers.name,
       Sales.amount, Sales.sale_date
FROM Sales
JOIN Salesmen ON Sales.salesman_id = Salesmen.id
JOIN Customers ON Sales.customer_id = Customers.id
ORDER BY Sales.id
""")


show_query(2, "Угоди продавця Bib", """
SELECT Sales.id, Salesmen.name, Customers.name,
       Sales.amount, Sales.sale_date
FROM Sales
JOIN Salesmen ON Sales.salesman_id = Salesmen.id
JOIN Customers ON Sales.customer_id = Customers.id
WHERE Salesmen.name = ?
""", ("Bib",))


show_query(3, "Максимальна угода", """
SELECT *
FROM Sales
WHERE amount = (SELECT MAX(amount) FROM Sales)
""")


show_query(4, "Мінімальна угода", """
SELECT *
FROM Sales
WHERE amount = (SELECT MIN(amount) FROM Sales)
""")


show_query(5, "Максимальна угода продавця Bib", """
SELECT MAX(amount)
FROM Sales
WHERE salesman_id = (
    SELECT id FROM Salesmen WHERE name = ?
)
""", ("Bib",))


show_query(6, "Мінімальна угода продавця Bib", """
SELECT MIN(amount)
FROM Sales
WHERE salesman_id = (
    SELECT id FROM Salesmen WHERE name = ?
)
""", ("Bib",))


show_query(7, "Максимальна покупка Bible", """
SELECT MAX(amount)
FROM Sales
WHERE customer_id = (
    SELECT id FROM Customers WHERE name = ?
)
""", ("Bible",))


show_query(8, "Мінімальна покупка Bible", """
SELECT MIN(amount)
FROM Sales
WHERE customer_id = (
    SELECT id FROM Customers WHERE name = ?
)
""", ("Bible",))


show_query(9, "Продавець з найбільшою сумою продажів", """
SELECT Salesmen.name, SUM(Sales.amount) AS total
FROM Sales
JOIN Salesmen ON Sales.salesman_id = Salesmen.id
GROUP BY Salesmen.id, Salesmen.name
ORDER BY total DESC
LIMIT 1
""")


show_query(10, "Продавець з найменшою сумою продажів", """
SELECT Salesmen.name, SUM(Sales.amount) AS total
FROM Sales
JOIN Salesmen ON Sales.salesman_id = Salesmen.id
GROUP BY Salesmen.id, Salesmen.name
ORDER BY total ASC
LIMIT 1
""")


show_query(11, "Покупець з найбільшою сумою покупок", """
SELECT Customers.name, SUM(Sales.amount) AS total
FROM Sales
JOIN Customers ON Sales.customer_id = Customers.id
GROUP BY Customers.id, Customers.name
ORDER BY total DESC
LIMIT 1
""")


show_query(12, "Середня сума покупки Bible", """
SELECT AVG(amount)
FROM Sales
WHERE customer_id = (
    SELECT id FROM Customers WHERE name = ?
)
""", ("Bible",))


show_query(13, "Середня сума продажу Bib", """
SELECT AVG(amount)
FROM Sales
WHERE salesman_id = (
    SELECT id FROM Salesmen WHERE name = ?
)
""", ("Bib",))


conn.close()
