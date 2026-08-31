# Завдання 1
# Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалі­зуйте:
# перевірку на рівність типів літаків (операція = =);
# збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
# порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=).
class Airplane:
    def __init__(self, airplane_type, passengers, max_passengers):
        self.airplane_type = airplane_type
        self.passengers = passengers
        self.max_passengers = max_passengers
    def show_info(self):
        print(f"Тип літака: {self.airplane_type}")
        print(f"Пасажирів: {self.passengers}")
        print(f"Максимум пасажирів: {self.max_passengers}")
    def __eq__(self, other):
        return self.airplane_type == other.airplane_type
    def __add__(self, amount):
        new_passengers = self.passengers + amount
        if new_passengers > self.max_passengers:
            new_passengers = self.max_passengers
        return Airplane(
            self.airplane_type,
            new_passengers,
            self.max_passengers
        )
    def __sub__(self, amount):
        new_passengers = self.passengers - amount
        if new_passengers < 0:
            new_passengers = 0
        return Airplane(
            self.airplane_type,
            new_passengers,
            self.max_passengers
        )
    def __iadd__(self, amount):
        self.passengers += amount
        if self.passengers > self.max_passengers:
            self.passengers = self.max_passengers
        return self
    def __isub__(self, amount):
        self.passengers -= amount
        if self.passengers < 0:
            self.passengers = 0
        return self
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers
    def __le__(self, other):
        return self.max_passengers <= other.max_passengers
    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers
plane1 = Airplane("Boeing 737", 100, 180)
plane2 = Airplane("Airbus A320", 120, 190)
plane3 = Airplane("Boeing 737", 150, 200)
print(plane1 == plane2)  # False
print(plane1 == plane3)  # True
print(plane1 < plane2)   # True
print(plane1 >= plane2)  # False
plane1 += 20
plane1.show_info()
plane1 -= 10
plane1.show_info()
plane4 = plane1 + 30
plane4.show_info()
plane5 = plane1 - 50
plane5.show_info()
# Завдання 2
# Створіть клас Flat (Квартира). Реалізуйте перевантажені оператори:
# перевірку на рівність площ квартир (операція ==);
# перевірку на нерівність площ квартир (операція !=);
# порівняння двох квартир за ціною (операції >, <, <=, >=).
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price
    def show_info(self):
        print(f"Площа: {self.area} м²")
        print(f"Ціна: {self.price}$")
    def __eq__(self, other):
        return self.area == other.area
    def __ne__(self, other):
        return self.area != other.area
    def __gt__(self, other):
        return self.price > other.price
    def __lt__(self, other):
        return self.price < other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
flat1 = Flat(50, 70000)
flat2 = Flat(50, 80000)
flat3 = Flat(70, 100000)
print(flat1 == flat2)  # True
print(flat1 != flat3)  # True
print(flat1 > flat2)   # False
print(flat1 < flat3)   # True
print(flat2 <= flat3)  # True
print(flat3 >= flat1)  # True
# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур. Визначте методи:
# Show() — виведення на екран інформації про фігуру;
# Save() — збереження фігури у файл;
# Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# Square — квадрат із заданими з координатами лівого верхнього кута та дов­жи­ною сторони.
# Rectangle — прямокутник із заданими координатами верхнього лівого кута та розмірами.
# Circle — коло із заданими координатами центру та радіусом.
# Ellipse — еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами, паралельними
# осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну фігуру.
class Shape:
    def Show(self):
        pass
    def Save(self, file):
        pass
    @staticmethod
    def Load(file_name):
        shapes = []
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(";")
                if data[0] == "Square":
                    shape = Square(
                        int(data[1]),
                        int(data[2]),
                        int(data[3])
                    )
                elif data[0] == "Rectangle":
                    shape = Rectangle(
                        int(data[1]),
                        int(data[2]),
                        int(data[3]),
                        int(data[4])
                    )
                elif data[0] == "Circle":
                    shape = Circle(
                        int(data[1]),
                        int(data[2]),
                        int(data[3])
                    )
                elif data[0] == "Ellipse":
                    shape = Ellipse(
                        int(data[1]),
                        int(data[2]),
                        int(data[3]),
                        int(data[4])
                    )
                shapes.append(shape)
        return shapes
class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    def Show(self):
        print("Square")
        print(f"Лівий верхній кут: ({self.x}, {self.y})")
        print(f"Сторона: {self.side}")
    def Save(self, file):
        file.write(
            f"Square;{self.x};{self.y};{self.side}\n"
        )
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def Show(self):
        print("Rectangle")
        print(f"Лівий верхній кут: ({self.x}, {self.y})")
        print(f"Ширина: {self.width}")
        print(f"Висота: {self.height}")
    def Save(self, file):
        file.write(
            f"Rectangle;{self.x};{self.y};"
            f"{self.width};{self.height}\n"
        )
class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def Show(self):
        print("Circle")
        print(f"Центр: ({self.x}, {self.y})")
        print(f"Радіус: {self.radius}")
    def Save(self, file):
        file.write(
            f"Circle;{self.x};{self.y};{self.radius}\n"
        )
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def Show(self):
        print("Ellipse")
        print(f"Лівий верхній кут: ({self.x}, {self.y})")
        print(f"Ширина прямокутника: {self.width}")
        print(f"Висота прямокутника: {self.height}")
    def Save(self, file):
        file.write(
            f"Ellipse;{self.x};{self.y};"
            f"{self.width};{self.height}\n"
        )
shapes = [
    Square(10, 20, 5),
    Rectangle(5, 10, 20, 30),
    Circle(50, 50, 15),
    Ellipse(15, 25, 40, 20)
]
with open("shapes.txt", "w", encoding="utf-8") as file:
    for shape in shapes:
        shape.Save(file)
loaded_shapes = Shape.Load("shapes.txt")
for shape in loaded_shapes:
    shape.Show()
    print("-" * 30)