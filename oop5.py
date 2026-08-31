from abc import ABC, abstractmethod


class AbstractBasePlayer(ABC):
    def __init__(self, name, rasa):
        self.name = name
        self.rasa = rasa

    @abstractmethod
    def atack(self):
        pass

    def show_info(self):
        print(f"Name: {self.name}\nRasa: {self.rasa}")


class Human(AbstractBasePlayer):
    def __init__(self, name, age):
        super().__init__(name, "human")
        self.age = age

    def atack(self):
        print("Human atack with sword!")

    def show_info(self):
        # print("Human show_info with sword!")
        super().show_info()
        print(f"age : {self.age}")


class Elf(AbstractBasePlayer):
    def __init__(self, name):
        super().__init__(name, "elf")

    def atack(self):
        print("Elf atack with bowl!")


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        if isinstance(player, AbstractBasePlayer) and player not in self.players:
            self.players.append(player)

    def show_players(self):
        if self.players:
            for player in self.players:
                player.show_info()

    def battle(self):
        if self.players:
            for player in self.players:
                player.atack()


h1 = Human("Max", 34)
h2 = Human("Bill", 54)

elf1 = Elf("Jin")

elf2 = Elf("Elfir")

game = Game()
game.add_player(elf1)
game.add_player(elf2)
game.add_player(h1)
game.add_player(h2)

game.show_players()
game.battle()

# 1
# Створіть абстрактний клас Transport.
# Атрибути:
# brand speed
# Методи:
# show_info() — звичайний метод;
# move() — абстрактний метод.
# Створіть:
# Car Plane Ship
# Кожен транспорт повинен по-своєму реалізувати move():
# Автомобіль їде дорогою.
# Літак летить у повітрі.
# Корабель пливе по воді.
# Створіть список різних транспортних засобів і за допомогою циклу викличте move() для кожного.

from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def show_info(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")
    @abstractmethod
    def move(self):
        pass
class Car(Transport):
    def move(self):
        print("Автомобіль їде дорогою")
class Plane(Transport):
    def move(self):
        print("Літак летить у повітрі")
class Ship(Transport):
    def move(self):
        print("Корабель пливе по воді")

car1 = Car("Mazda", 220)
plane1 = Plane("Boeing", 900)
ship1 = Ship("MSC", 40)
transports = [car1, plane1, ship1]
for transport in transports:
    transport.show_info()
    transport.move()

print(type(type(type(elf1))))

class pet:
    pass
print(type(type(pet)))

# metaclass

class MyMetaClass(type):
    def __new__(cls, name, bases, dict):
        print("Hello from __new__()")
        print(f"type of the class created {cls}")
        print(f"name: {name}")
        print(f"bases: {bases}")
        print(f"dict: {dict}")
        return super().__new__(cls, name, bases, dict)


class MyMetaClass1(type):
    def __new__(cls, name, bases, dict):
        if 'id' not in dict.keys():
            # print(f"No id attribute in class {name}")
            print("add id attr")
            setattr(cls, "id", id)

            methods = {key: value for key, value in dict.items() if callable(value)}
            if len(methods) > 2:
                print(f"Error more then 2 method in class {name}")
            else:
                print(f"Class {name} is creating")
                return super().__new__(cls, name, bases, dict)


class MyClas1(metaclass=MyMetaClass1):
    attr = 100



class MClass2(metaclass=MyMetaClass1):
    name = "sdfs"
    num = 0

# 2
# Створіть метаклас MyMeta, який під час створення нового класу виводить:
# Створюється клас: <назва класу>
# За допомогою цього метакласу створіть класи:
# class Student(metaclass=MyMeta):
#     passclass Teacher(metaclass=MyMeta):
#     pass
class MyMeta(type):
    def __new__(cls, name, bases, dict):
        return super().__new__(cls, name, bases, dict)
class Student(metaclass=MyMeta):
    pass
class Teacher(metaclass=MyMeta):
    pass

# 3
# Створіть метаклас RequiredMethodMeta.
# Він повинен перевіряти, чи містить створюваний клас метод:
# show_info()
# Якщо методу немає — заборонити створення класу за допомогою:
# raise TypeError(...)

class RequiredMethodMeta(type):
    def __new__(cls, name, bases, dict):
        if "show_info" not in dict.keys():
            raise TypeError(f"No show_info method in class {name}")
        return super().__new__(cls, name, bases, dict)
class Student(metaclass=RequiredMethodMeta):
    def show_info(self):
        print("Student info")