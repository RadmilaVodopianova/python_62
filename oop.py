# name="Bob"
# health=100
# damage=20
#
# print(name)
# print(health)
# print(damage)
#
# name2="Bob"
# health2=100
# damage2=20
#
# print(name2)
# print(health2)
# print(damage2)
#
# player1={
#     "name":"Bob",
#     "health":100,
#     "damage":20
# }
#
# def atack(player):
#     print(f"{player} atack")

# number=100
# print(type(number))
class Player:
    name = ""
    def stack(self):
        print(f"atack")
p1=Player()
p1.name = "Rada"
print(p1.name)

class Car:
    speed = 0
    color = "black"

car1 = Car()
car2 = Car()
print(car1.color)
print(car2.color)

car1.speed = 100
car2.color='red'
print(car2.color)
print(car1.color)

class Player:

    def __init__(self, name='user'):
        self.name = name
        self.login = "qwerty"
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
new_player1 = Player('Max')
print(new_player1.name)
new_player1.name = 'error'
print(new_player1.name)


class Student:
    def __init__(self, name, age,av_grade):
        self.name = name
        self.age = age
        self.av_grade = av_grade
    def get_name(self, new_name):
        self.name = new_name
    def get_age(self, new_age):
        self.age = new_age
    def get_av_grade(self, new_av_grade):
        self.av_grade = new_av_grade
student1 = Student('Bib', 20,'4')
print(student1.name)
student1.get_name("Bob")
print(student1.name)
student1.get_age(23)
print(student1.age)
student1.get_av_grade(5)
print(student1.av_grade)


