# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину),
# клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи.
class Device:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def show_info(self):
        print(f"Назва: {self.name}")
        print(f"Потужність: {self.power} Вт")
    def turn_on(self):
        print(f"{self.name} увімкнено")
    def turn_off(self):
        print(f"{self.name} вимкнено")
class CoffeeMachine(Device):
    def __init__(self, name, power, coffee_type):
        super().__init__(name, power)
        self.coffee_type = coffee_type
    def make_coffee(self):
        print(f"Кавомашина готує {self.coffee_type}")
class Blender(Device):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed
    def blend(self):
        print(f"Блендер працює на швидкості {self.speed}")
class MeatGrinder(Device):
    def __init__(self, name, power, meat_type):
        super().__init__(name, power)
        self.meat_type = meat_type
    def grind_meat(self):
        print(f"М'ясорубка перемелює {self.meat_type}")
coffee_machine = CoffeeMachine("Philips", 1500, "капучино")
coffee_machine.show_info()
coffee_machine.turn_on()
coffee_machine.make_coffee()
print()
blender = Blender("Bosch", 800, 3)
blender.show_info()
blender.turn_on()
blender.blend()
print()
meat_grinder = MeatGrinder("Samsung", 1200, "свинину")
meat_grinder.show_info()
meat_grinder.turn_on()
meat_grinder.grind_meat()
# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі. За допомогою механізму успадкування реалізуйте клас Frigate
# (містить інформацію про фрегат), клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію про крейсер).
# Кожен із класів має містити необхідні для роботи методи.
class Ship:
    def __init__(self, name, speed, crew):
        self.name = name
        self.speed = speed
        self.crew = crew
    def show_info(self):
        print(f"Назва корабля: {self.name}")
        print(f"Швидкість: {self.speed} вузлів")
        print(f"Екіпаж: {self.crew} осіб")
    def move(self):
        print(f"Корабель {self.name} рухається")
    def stop(self):
        print(f"Корабель {self.name} зупинився")
class Frigate(Ship):
    def __init__(self, name, speed, crew, missiles):
        super().__init__(name, speed, crew)
        self.missiles = missiles
    def attack(self):
        print(f"Фрегат {self.name} атакує. Ракет: {self.missiles}")
class Destroyer(Ship):
    def __init__(self, name, speed, crew, guns):
        super().__init__(name, speed, crew)
        self.guns = guns
    def attack(self):
        print(f"Есмінець {self.name} атакує з {self.guns} гармат")
class Cruiser(Ship):
    def __init__(self, name, speed, crew, helicopters):
        super().__init__(name, speed, crew)
        self.helicopters = helicopters
    def attack(self):
        print(f"Крейсер {self.name} атакує. Гелікоптерів: {self.helicopters}")
frigate = Frigate("FOne", 30, 180, 16)
frigate.show_info()
frigate.move()
frigate.attack()
print()
destroyer = Destroyer("DOne", 32, 300, 6)
destroyer.show_info()
destroyer.move()
destroyer.attack()
print()
cruiser = Cruiser("COne", 30, 500, 2)
cruiser.show_info()
cruiser.move()
cruiser.attack()
# Завдання 3
# Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок
# (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def show_amount(self):
        print(f"{self.dollars}.{self.cents:02d}")
    def set_dollars(self, dollars):
        self.dollars = dollars
    def set_cents(self, cents):
        self.cents = cents
class Product(Money):
    def __init__(self, name, dollars, cents):
        super().__init__(dollars, cents)
        self.name = name
    def show_product(self):
        print(f"Товар: {self.name}")
        print(f"Ціна: {self.dollars}.{self.cents:02d}")
    def reduce_price(self, dollars, cents):
        total = self.dollars * 100 + self.cents
        discount = dollars * 100 + cents
        total -= discount
        self.dollars = total // 100
        self.cents = total % 100
money = Money(100, 50)
print("Сума:")
money.show_amount()
money.set_dollars(200)
money.set_cents(75)
print("Нова сума:")
money.show_amount()
print()
product = Product("Ноутбук", 750, 20)
product.show_product()
product.reduce_price(100, 10)
print("Після знижки:")
product.show_product()
# Завдання 4
# Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки. У класі має знаходитися два статичні методи:
#  для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розра­хувати кількість
# підрахунків температури та повернути це значення статичним методом.
class Temperature:
    count = 0
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        Temperature.count += 1
        return celsius * 9 / 5 + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        Temperature.count += 1
        return (fahrenheit - 32) * 5 / 9
    @staticmethod
    def get_count():
        return Temperature.count
print(Temperature.celsius_to_fahrenheit(25))
print(Temperature.fahrenheit_to_celsius(77))
print(Temperature.celsius_to_fahrenheit(100))
print("Кількість конвертацій:", Temperature.get_count())
