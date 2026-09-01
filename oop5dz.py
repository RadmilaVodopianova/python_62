# Завдання 1. Працівники компанії
# Створіть абстрактний клас Employee.
# Атрибути: name, salary
# Абстрактний метод: work()
# Звичайний метод: show_info()
# Створіть класи:
# Programmer
# Designer
# Manager
# Реалізуйте work():
# Programmer пише код.
# Designer створює дизайн.
# Manager керує командою.
# Додатково додайте абстрактний метод:
# calculate_bonus()
# Наприклад:
# Programmer — 15% зарплати;
# Designer — 10%;
# Manager — 20%.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def calculate_bonus(self):
        pass
class Programmer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("Programmer writes code")
    def calculate_bonus(self):
        return self.salary * 0.15
class Designer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("Designer creates design")
    def calculate_bonus(self):
        return self.salary * 0.10
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("Manager manages team")
    def calculate_bonus(self):
        return self.salary * 0.20
programmer1 = Programmer("Bob", 3000)
designer1 = Designer("Bib", 2500)
manager1 = Manager("Bill", 4000)
employees = [programmer1, designer1, manager1]
for employee in employees:
    employee.show_info()
    employee.work()
    print(f"Bonus: {employee.calculate_bonus()}")
    print()
# Завдання 2 : Реалізація системи перевірки правил для класів за допомогою метакласів
# Опис завдання:
# Вам потрібно створити систему, яка забезпечує автоматичну перевірку, чи відповідають створені класи певним вимогам.
# Для цього потрібно використовувати метакласи.
# Вимоги до завдання:
# Створіть метаклас ValidationMeta:
# Перевіряйте, чи всі методи класу починаються зі слова do_ (наприклад, do_task, do_something_else).
# Перевіряйте, чи є в класі атрибут description, і чи є він рядком.
# Створіть базовий клас ValidatedClass:
# Визначте цей клас із використанням метакласу ValidationMeta.
# Створіть кілька класів, які наслідують ValidatedClass:
# Один клас повинен відповідати всім правилам.
# Інший клас має порушувати одне з правил (наприклад, методи не починаються з do_ або відсутній атрибут description).
# Додайте виключення:
# Якщо клас порушує правила метакласу, має бути викликана помилка ValueError із поясненням, що саме не відповідає вимогам.
# Реалізуйте програму, яка створює об'єкти цих класів:
# У програмі виведіть інформацію про те, чи успішно створено кожен клас, або ж, якщо є помилка, виведіть її текст.
# Додаткові вимоги:
# Використовуйте модуль abc для визначення базового класу.
# Додайте можливість автоматичного створення відсутнього атрибуту description з дефолтним значенням, якщо його немає.
from abc import ABC, abstractmethod, ABCMeta
class ValidationMeta(ABCMeta):
    def __new__(cls, name, bases, dict):
        if name != "ValidatedClass":
            if "description" not in dict.keys():
                print(f"Add description in class {name}")
                dict["description"] = "No description"
            if not isinstance(dict["description"], str):
                raise ValueError(
                    f"description in class {name} must be string"
                )
            methods = {
                key: value for key, value in dict.items()
                if callable(value) and not key.startswith("__")
            }
            for method in methods.keys():
                if not method.startswith("do_"):
                    raise ValueError(
                        f"Method {method} in class {name} must start with do_"
                    )
        return super().__new__(cls, name, bases, dict)
class ValidatedClass(ABC, metaclass=ValidationMeta):
    @abstractmethod
    def do_task(self):
        pass
try:
    class GoodClass(ValidatedClass):
        description = "Good class"
        def do_task(self):
            print("Doing task")
        def do_work(self):
            print("Doing work")
    good1 = GoodClass()
    print("GoodClass created")
    print(good1.description)
    good1.do_task()
    good1.do_work()
except ValueError as error:
    print(error)
print()
try:
    class SecondClass(ValidatedClass):
        def do_task(self):
            print("Doing task")
    second1 = SecondClass()
    print("SecondClass created")
    print(second1.description)
except ValueError as error:
    print(error)
print()
try:
    class BadClass(ValidatedClass):
        description = "Bad class"

        def do_task(self):
            print("Doing task")

        def work(self):
            print("Working")
    bad1 = BadClass()
except ValueError as error:
    print(error)