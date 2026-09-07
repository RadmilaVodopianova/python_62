# Домашня робота. Стек
# Рівень 1
# Завдання 1. Розвантаження вантажівки
# Коробки завантажували у вантажівку в такому порядку:
# Box 1
# Box 2
# Box 3
# Box 4
# Box 5
# Збережіть коробки у стек.
# Після цього розвантажте всі коробки, використовуючи pop().
# Програма повинна виводити:
# Розвантажено: Box 5
# Розвантажено: Box 4
# Розвантажено: Box 3
# Розвантажено: Box 2
# Розвантажено: Box 1
# Наприкінці виведіть: Вантажівка порожня
# Перед запуском програми поясніть у коментарі, чому Box 5 буде розвантажено першою.
class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
boxes = Stack()
boxes.push("Box 1")
boxes.push("Box 2")
boxes.push("Box 3")
boxes.push("Box 4")
boxes.push("Box 5")
while not boxes.is_empty():
    print(f"Розвантажено: {boxes.pop()}")
print("Вантажівка порожня")

# Завдання 2. Перевертач тексту
# Користувач вводить будь-який текст:
# Hello Python
# Додайте кожен символ рядка до стека.
# Потім, використовуючи тільки pop(), сформуйте рядок у зворотному порядку.
# Результат:
# nohtyP olleH
# Не можна використовувати: [::-1]
# Додатково
# Перевірте за допомогою стека, чи є введене слово паліндромом.
# Наприклад:
# level → паліндром
# python → не паліндром
text = input("Введіть текст: ")
text_stack = Stack()
for symbol in text:
    text_stack.push(symbol)
reversed_text = ""
while not text_stack.is_empty():
    reversed_text += text_stack.pop()
print(reversed_text)
word = input("Введіть слово: ").lower()
word_stack = Stack()
for symbol in word:
    word_stack.push(symbol)
reversed_word = ""
while not word_stack.is_empty():
    reversed_word += word_stack.pop()
if word == reversed_word:
    print("Паліндром")
else:
    print("Не паліндром")

# Завдання 3 — «Паркування автомобілів»
# Уявіть вузьку парковку, де автомобілі стоять один за одним і виїхати першим може тільки останній автомобіль, який заїхав.
# Створіть клас Parking, який використовує об'єкт класу Stack.
# class Parking:
#     def __init__(self, max_cars):
#         self.cars = Stack()
#         self.max_cars = max_cars
#     # реалізуйте методи
# Необхідно реалізувати:
# park(car) — автомобіль заїжджає на парковку;
# leave() — останній автомобіль залишає парковку;
# last_car() — показати автомобіль, який може виїхати наступним;
# is_full() — перевірити, чи заповнена парковка;
# show_count() — показати кількість автомобілів.
# При виборі Undo остання дія повинна видалятися зі стека.
# Наприклад:
# Стек:
# Додано текст
# Змінено колір
# Додано зображення ← TOP
# Після Undo:
# Скасовано: Додано зображення
# Новою вершиною буде:
# Змінено колір
# Обов'язково передбачте ситуацію, коли користувач намагається виконати Undo, але стек уже порожній.
class Parking:
    def __init__(self, max_cars):
        self.cars = Stack()
        self.max_cars = max_cars
    def park(self, car):
        if self.is_full():
            return False
        self.cars.push(car)
        return True
    def leave(self):
        return self.cars.pop()
    def last_car(self):
        return self.cars.peek()
    def is_full(self):
        return self.cars.size() >= self.max_cars
    def show_count(self):
        return self.cars.size()
parking = Parking(3)
print(parking.park("Car 1"))
print(parking.park("Car 2"))
print(parking.park("Car 3"))
print(parking.is_full())
print(parking.park("Car 4"))
print(parking.last_car())
print(parking.show_count())
print(parking.leave())
print(parking.last_car())
print(parking.show_count())
print(parking.leave())
print(parking.leave())
print(parking.leave())
class Editor:
    def __init__(self):
        self.history = Stack()
    def add_action(self, action):
        self.history.push(action)
    def undo(self):
        if self.history.is_empty():
            return None
        return self.history.pop()
    def last_action(self):
        return self.history.peek()
editor = Editor()
editor.add_action("Додано текст")
editor.add_action("Змінено колір")
editor.add_action("Додано зображення")
action = editor.undo()
if action is None:
    print("Немає дій для скасування")
else:
    print(f"Скасовано: {action}")
last = editor.last_action()
if last is None:
    print("Стек порожній")
else:
    print(f"Новою вершиною буде: {last}")
editor.undo()
editor.undo()
action = editor.undo()
if action is None:
    print("Немає дій для скасування")
else:
    print(f"Скасовано: {action}")