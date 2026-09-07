# Домашня робота. Пов’язані списки
# Рівень 1
# Завдання 1. Ланцюжок міст
# Створіть клас Node.
# Створіть вручну 4 вузли зі значеннями:
# Київ
# Львів
# Одеса
# Харків
# Пов’яжіть їх у такому порядку:
# Київ → Львів → Одеса → Харків → None
# Виведіть:
# перше місто;
# друге місто;
# третє місто;
# четверте місто.
# При цьому для виведення використовуйте тільки змінну першого вузла.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node("Київ")
node2 = Node("Львів")
node3 = Node("Одеса")
node4 =  Node("Харків")
node1.next = node2
node2.next = node3
node3.next = node4
print(node1.data)
print(node1.next.data)
print(node1.next.next.data)
print(node1.next.next.next.data)
# Завдання 2. Пройдіть по всьому списку
# Створіть однозв’язний список:
# 10 → 25 → 40 → 55 → 70 → None
# Не виводьте кожен вузол окремо через:
# node1.next.next...
# Замість цього використайте змінну:
# current
# та цикл while.
# Програма повинна вивести:
# 10
# 25
# 40
# 55
# 70
# Додатково: порахуйте кількість вузлів у списку.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
num_nodes = LinkedList()
num_nodes.add_last(10)
num_nodes.add_last(25)
num_nodes.add_last(40)
num_nodes.add_last(55)
num_nodes.add_last(70)
num_nodes.show()
print(num_nodes.count())
# Рівень 2
# Завдання 3. Список улюблених фільмів
# Створіть класи:
# Node
# LinkedList
# У класі LinkedList реалізуйте метод:
# add_first()
# Додайте до списку:
# Interstellar
# Dune
# Avatar
# Titanic
# Після цього виведіть весь список.
# Перед запуском програми напишіть у коментарі, в якому порядку, на вашу думку, будуть розташовані фільми.
# Наприклад:
# Я думаю, що результат буде:
# Titanic
# Avatar
# Dune
# Interstellar
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
films = LinkedList()
films.add_first("Interstellar")
films.add_first("Dune")
films.add_first("Avatar")
films.add_first("Titanic")
films.show()
# Завдання 4. Пошук студента
# Створіть однозв’язний список студентів:
# Анна → Максим → Ірина → Олексій → Марія
# Додайте до класу LinkedList метод:
# contains(value)
# Метод повинен повертати:
# True якщо значення знайдено, та:
# False якщо його немає.
# Приклад:
# students.contains("Ірина")
# Результат: True
# А: students.contains("Денис")
# Результат: False
# Додатково: зробіть так, щоб користувач сам вводив ім’я для пошуку.
# Завдання 4. Пошук студента

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def contains(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False
students = LinkedList()
students.add_last("Анна")
students.add_last("Максим")
students.add_last("Ірина")
students.add_last("Олексій")
students.add_last("Марія")
print(students.contains("Ірина"))
print(students.contains("Денис"))
name = input("Введіть ім'я студента для пошуку: ")
print(students.contains(name))
