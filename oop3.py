import random
import datetime

class Person:
    def __init__(self, name, age):
        if Person.validate_name(name):
            self.name = name
        else:
            self.name = "Unknown"

        # protected prop
        self._age = age

        # private prop
        self.__person_id = random.randint(1, 100)

    def get_info(self):
        self.__show_id()
        return f"{self.name} is {self._age} years old"

    @staticmethod
    def getHi(text):
        return f"{text}!"

    def _get_name(self):
        return self.name

    def __show_id(self):
        print(self.__person_id)

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def validate_name(name):
        return len(name) >= 2

    def show_name(self):
        if Person.validate_name(self.name):
            print(self.name)

    @classmethod
    def setDefaultHobby(cls, hobby):
        cls.hobby = hobby

    @classmethod
    def basedOnYear(cls, name, bYear):
        personAge = datetime.date.today().year - bYear
        return cls(name, personAge)


p1 = Person("Dill", 18)

print(p1.getHi("Hi"))
print(Person.getHi("test class"))
print(Person.is_adult(20))

newperson = Person.basedOnYear("Max", 2005)
print(newperson.get_info())
Person.setDefaultHobby("Cooking")
print(newperson.hobby)
class Math:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def sub(x, y):
        return x - y
    @staticmethod
    def mul(x, y):
        return x * y
print(Math.add(1, 2))
math = Math()

# Завдання — клас BankAccount
# Створіть клас BankAccount, який буде описувати банківський рахунок.
# У класі мають бути атрибути:
# owner       # ім'я власникаbalance     # баланс рахунку
# Реалізуйте такі методи:
# show_info() — виводить ім'я власника та поточний баланс.
# deposit(amount) — поповнює рахунок на вказану суму.
# withdraw(amount) — знімає гроші з рахунку.
# Якщо грошей недостатньо — вивести відповідне повідомлення.
# transfer(amount, other_account) — переводить гроші на інший рахунок.
# Перевірити, чи достатньо коштів.
# add_bonus(percent) — збільшує баланс на заданий відсоток.
# is_empty() — повертає True, якщо баланс дорівнює 0, інакше False.

# До вже створеного BankAccount додати:
# Атрибут класу bank_name = "Python Bank".
# Атрибут класу account_count = 0.
# Зробити так, щоб після створення кожного нового рахунку account_count збільшувався на 1.
# Створити @classmethod show_account_count(), який показує кількість створених рахунків.
# Створити @classmethod change_bank_name(new_name), який змінює назву банку для всіх рахунків.
# Створити @classmethod show_bank_name(), який показує поточну назву банку.
class BankAccount:
    bank_name="Python Bank"
    account_count = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.account_count += 1
    def show_info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <=0:
            print("You cannot withdraw negative amount")
        elif self.balance < amount:
            print("Not enough money")
        else:
            self.balance -= amount
    def transfer(self,amount,other_account):
        if amount <=0:
            print("You cannot withdraw negative amount")
        elif self.balance < amount:
            print("Not enough money")
        else:
            self.balance -= amount
            other_account.balance += amount
    @classmethod
    def show_account_count(cls):
        print(f"Account count:{cls.account_count}")
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name}")
    @classmethod
    def show_bank_name(cls):
        print(f"Bank name {cls.bank_name}")
account1=BankAccount("Bib",12500580)
account2=BankAccount("Bob",12560580)
account1.show_info()
BankAccount.show_account_count()

class MyBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_book_info(self):
        print(self.title)
        print(self.author)
        print(self.pages)
class MyFile:
    def __init__(self,file_size,scr):
        self.file_size = file_size
        self.scr = scr
    def get_file_info(self):
        print(self.file_size)
        print(self.scr)
class MyEBook(MyBook,MyFile):
    def __init__(self,file_size,scr):
        MyBook.__init__(self,file_size,scr)
        MyFile.__init__(self,file_size,scr)
eBook1=MyEBook("python","Gvido",356)
eBook1.get_book_info()
eBook1.get_file_info()


# Створіть два батьківські класи:
# Клас Phone:
# phone_number — номер телефону;
# метод call(number) — виводить повідомлення про дзвінок;
# метод show_phone_info() — показує номер телефону.
# Клас Camera:
# megapixels — кількість мегапікселів;
# метод take_photo() — виводить повідомлення про створення фотографії;
# метод show_camera_info() — показує характеристики камери.
# Створіть клас:
# class Smartphone(Phone, Camera):
# Він повинен успадковувати можливості одночасно від Phone і Camera.
# У Smartphone додайте власні атрибути:
# brandmodel
# та метод:
# show_info()
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def call(self, number):
        print(f"Calling {number}")
    def show_phone_info(self):
        print(f"Phone number: {self.phone_number}")
class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    def take_photo(self):
        print("Photo taken")
    def show_camera_info(self):
        print(f"Camera: {self.megapixels} MP")
class Smartphone(Phone, Camera):
    def __init__(self, phone_number, megapixels, brand, model):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, megapixels)
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Phone number: {self.phone_number}")
        print(f"Camera: {self.megapixels} MP")
smartphone1 = Smartphone("+38000000000", 72, "IPhone", "121")
smartphone1.show_info()
smartphone1.call("+38000500005")
smartphone1.take_photo()
smartphone1.show_phone_info()
smartphone1.show_camera_info()



