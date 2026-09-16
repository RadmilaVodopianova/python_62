# Створіть програму для роботи з каталогом товарів, використовуючи бінарне дерево пошуку (Binary Search Tree).
# Кожен товар повинен бути окремим об'єктом класу Product.
# Клас Product повинен містити:
# id — унікальний номер товару;
# name — назву товару;
# price — ціну товару.
# Приклад товарів:
# ID: 50 — Laptop
# ID: 25 — Mouse
# ID: 75 — Monitor
# ID: 10 — Cable
# ID: 35 — Keyboard
# ID: 60 — Headphones
# Дерево потрібно організувати за полем id.
# Правило додавання:
# менший ID → ліворуч
# більший ID → праворуч
# У результаті може утворитися таке дерево:
#
#              50 Laptop
#             /         \
#        25 Mouse       75 Monitor
#        /     \         /
#  10 Cable  35 Keyboard 60 Headphones
# Необхідно реалізувати
# Створіть класи:
# Product
# Node
# ProductTree
# У класі ProductTree реалізуйте методи:
# add_product(product)
# find_product(id)
# contains(id)
# show_products()
# Програма повинна вміти:
# Додавати новий товар у дерево.
# Не дозволяти додавати два товари з однаковим id.
# Знаходити товар за його id.
# Перевіряти, чи існує товар із заданим id.
# Виводити всі товари каталогу.
# Під час виведення показувати id, назву та ціну товару.
# Приклад роботи
# Каталог товарів:
# 10 — Cable — 250 грн
# 25 — Mouse — 800 грн
# 35 — Keyboard — 1500 грн
# 50 — Laptop — 30000 грн
# 60 — Headphones — 2000 грн
# 75 — Monitor — 12000 грн
# При пошуку:
# Введіть ID товару: 35
# Товар знайдено:
# Keyboard
# Ціна: 1500 грн
# Якщо товару немає:
# Введіть ID товару: 100
# Товар не знайдено
# Додатково
# Для тих, хто виконає основну частину:
# додайте метод пошуку найдешевшого товару;
# додайте метод пошуку найдорожчого товару;
# реалізуйте підрахунок кількості товарів у дереві;
# додайте консольне меню для роботи з каталогом.

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id} — {self.name} — {self.price} грн"


class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class ProductTree:
    def __init__(self):
        self.root = None

    def add_product(self, product):
        if self.root is None:
            self.root = Node(product)
            return True

        current = self.root

        while current is not None:
            if product.id == current.product.id:
                return False

            if product.id < current.product.id:
                if current.left is None:
                    current.left = Node(product)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(product)
                    return True
                current = current.right

    def find_product(self, id):
        current = self.root

        while current is not None:
            if id == current.product.id:
                return current.product

            if id < current.product.id:
                current = current.left
            else:
                current = current.right

        return None

    def contains(self, id):
        return self.find_product(id) is not None

    def show_products(self):
        if self.root is None:
            print("Каталог порожній")
            return

        self._show_products(self.root)

    def _show_products(self, node):
        if node is None:
            return

        self._show_products(node.left)
        print(node.product)
        self._show_products(node.right)


tree = ProductTree()

tree.add_product(Product(50, "Laptop", 30000))
tree.add_product(Product(25, "Mouse", 800))
tree.add_product(Product(75, "Monitor", 12000))
tree.add_product(Product(10, "Cable", 250))
tree.add_product(Product(35, "Keyboard", 1500))
tree.add_product(Product(60, "Headphones", 2000))

print("Каталог товарів:")
tree.show_products()

print("\nТовар з ID 35 існує:", tree.contains(35))
print("Товар з ID 100 існує:", tree.contains(100))

product_id = int(input("\nВведіть ID товару: "))
product = tree.find_product(product_id)

if product is not None:
    print("Товар знайдено:")
    print(product.name)
    print(f"Ціна: {product.price} грн")
else:
    print("Товар не знайдено")