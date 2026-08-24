# Створити три класи: Кішка (Cat),
# Собака (Dog) та Корова (Cow). Визначити
# такі атрибути об'єкта: ім'я (__name) вік
# (__age) колір (__color) Створити конструктор
# з трьома параметрами та три властивості
# (тільки гетери)
import random


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def golos(self):
        print("animal golos")

    def get_info(self):
        print(self.name)
        print(self.age)
        print(self.color)

class Dog(Animal):
    def __init__(self, name, age,color):
        print("Start creating the Dog")
        super().__init__(name,age,color)

    def golos(self):
        print("Gav gav")

class Cat(Animal):
    def __init__(self, name, age, color):
        print("Start creating the Cat")
        super().__init__(name, age, color)

    def golos(self):
        print("Meow meow")

class Cow(Animal):
    def __init__(self, name, age, color):
        print("Start creating the Cow")
        super().__init__(name, age, color)

    def golos(self):
        print("Moo moo")


dog1 = Dog("Dog1", 10, "blue")
dog1.golos()
dog1.get_info()

cat1 = Cat("Cat1", 5, "white")
cat1.golos()
cat1.get_info()

cow1 = Cow("Cow1", 7, "black")
cow1.golos()
cow1.get_info()

print(type(dog1))
print(type(type(dog1)))
print(type(cat1))
print(type(type(type(cat1))))




class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__person_id = random.randint(1, 100)

    def get_info(self):
        self.__show_id()
        return f"{self.name} is {self._age} years old"

    def getHi(self, text):
        return f"{text}! I am {self.name}"

    def _get_name(self):
        return self.name

    def __show_id(self):
        print(self.__person_id)


person1 = Person("John", 20)
print(person1.getHi("Hi"))


class Student(Person):
    spec = "Computer science"

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def isSuccessfull(self):
        return True if self.score >= 75 else False

    def get_info(self):
        return super().get_info() + f" score is {self.score}"


student1 = Student("Bill", 20, 78)
print(student1.getHi("Hi"))
print(student1.get_info())
print(student1.isSuccessfull())

st2 = Student("Nick", 19, 45)
print(st2.getHi("Hi"))
print(st2.get_info())
print(st2.isSuccessfull())


class Employee(Person):
    def __init__(self, name, age, salary, jobTitle):
        super().__init__(name, age)
        self.salary = salary
        self.jobTitle = jobTitle

    def get_info(self):
        return super().get_info() + f" salary is {self.salary}, jobTitle is {self.jobTitle}"

def change_age(self,new_age):
    self.age = new_age
print("____________________-")
p1=Person("John", 20)
print(p1._get_name())

manager=Employee("Bill",20,1000,"manager")
print(manager.get_info())
manager.change_age(35)
print(manager.get_info())


# 1) Створіть клас паспорт де будуть описані
# паспортні дані та на його основі створити загран
# паспорт

class Passport:
    def __init__(self, name, age, sex, passport_number):
        self.name = name
        self.age = age
        self.sex = sex
        self.passport_number = passport_number
    def get_info(self):
        return f"{self.name}, {self.age}, {self.sex}, {self.passport_number}"
class ForeignPassport(Passport):
    def __init__(self, name, age, sex, passport_number, nation):
        super().__init__(name, age, sex, passport_number)
        self.nation = nation
    def get_info(self):
        return super().get_info() + f", nation: {self.nation}"
p1 = Passport("Bella", 25, "female", "AI20205")
print(p1.get_info())
foreign1 = ForeignPassport("Bella", 25, "female", "FO05454", "Ukraine")
print(foreign1.get_info())


# Створіть базовий клас:
# Character
# Атрибути:
# name health damage
# Методи:
# show_info()attack()take_damage(amount)
# Потім створіть:
# Warrior(Character)Mage(Character)Archer(Character)
# Кожен клас повинен мати додатковий атрибут:
# Warrior → armor
# Mage → mana
# Archer → arrows
# Перевизначте attack() для кожного персонажа:
# Warrior Alex attacks with

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def show_info(self):
        return f"{self.name}, health: {self.health}, damage: {self.damage}"
    def attack(self):
        return f"{self.name} attacks"
    def take_damage(self, amount):
        self.health -= amount
class Warrior(Character):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage)
        self.armor = armor
    def attack(self):
        return f"Warrior {self.name} attacks with sword"
class Mage(Character):
    def __init__(self, name, health, damage, mana):
        super().__init__(name, health, damage)
        self.mana = mana
    def attack(self):
        return f"Mage {self.name} attacks with magic"
class Archer(Character):
    def __init__(self, name, health, damage, arrows):
        super().__init__(name, health, damage)
        self.arrows = arrows
    def attack(self):
        return f"Archer {self.name} attacks with bow"
warrior = Warrior("Bib", 100, 20, 50)
mage = Mage("Bob", 80, 30, 100)
archer = Archer("Bill", 90, 25, 20)
print(warrior.show_info())
print(warrior.attack())
print(mage.show_info())
print(mage.attack())
print(archer.show_info())
print(archer.attack())



