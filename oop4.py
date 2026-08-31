class Film:
    def __init__(self, title,director,age):
        self.title = title
        self.director = director
        self.age = age

    def showInfo(self):
        print(self.title)
        print(self.director)
        print(self.age)
class Book:
    def __init__(self, title, director, pages):
        self.title = title
        self.director = director
        self.pages = pages

    def showInfo(self):
        print(self.title)
        print(self.director)
        print(self.pages)

    def __str__(self) -> str:
        return f"{self.title} {self.director}, {self.pages}"

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __eq__(self, other):
        return self.title == other.title and self.director == other.director

    def __ne__(self, other):
        return self.title != other.title or self.director != other.director


film1 =Film("Python","Max",18)
book1 =Book("Python","Max",18)
for item in (film1,book1):
    item.showInfo()

class Class1:
    def __new__(cls):
        print("Hi i am __new__ magic method!")
        return super(Class1,cls).__new__(cls)
    def __init__(self):
        print("Hi i am __init__ magic method!")
obj1=Class1()

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("error multiplication")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.x += other
            self.y += other
            return self
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError("error addition")

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)
print(p2)

print(p1 * p2)
print(p1 * 2)

a = 1
a += 10
print(a)

print(p1)
p1 += 1
print(f"{p1}")



# Завдання 1
# Створіть (або використайте раніше створений) клас
# «Число». Клас «Число» зберігає всередині одне
# значення. Використовуючи перевантаження операторів,
# реалізуйте для нього арифметичні операції для роботи
# з числом (операції +, -, *, /).
class Number:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value}"
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
n1 = Number(10)
n2 = Number(5)
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
# авдання 2
# Створіть клас «Бібліотека». Клас призначений для збереження інформації про бібліотеку (назва, адреса, кількість книг і т.д.). Реалізуйте потрібні для класу способи. Використовуючи перевантаження операторів, реалізуйте для нього наступні арифметичні операції:
# + — додає до кількості книг вказане значення;
# - — віднімає з кількості книг вказане значення;
# += —додає до кількості книг вказане значення;
# -= — віднімає з кількості книг вказане значення.
# Використовуючи перевантаження операторів, реалізуйте (порівняння за кількістю книг):
# <;
# >;
# <=;
# >=;
# ==;
# !=.
class Library:
    def __init__(self, name, address, books):
        self.name = name
        self.address = address
        self.books = books
    def __str__(self):
        return f"{self.name}, {self.address}, books: {self.books}"
    def __add__(self, other):
        return Library(self.name, self.address, self.books + other)
    def __sub__(self, other):
        return Library(self.name, self.address, self.books - other)
    def __iadd__(self, other):
        self.books += other
        return self
    def __isub__(self, other):
        self.books -= other
        return self
    def __lt__(self, other):
        return self.books < other.books
    def __gt__(self, other):
        return self.books > other.books
    def __le__(self, other):
        return self.books <= other.books
    def __ge__(self, other):
        return self.books >= other.books
    def __eq__(self, other):
        return self.books == other.books
    def __ne__(self, other):
        return self.books != other.books


lib1 = Library("Library1", "street 12", 1000)
lib2 = Library("Library2", "street 13", 1001)

print(lib1)
print(lib2)





