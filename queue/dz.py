# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера. Мають бути клієнти, які надсилають запити на сервер, кожен з яких має свій пріоритет.
# Кожен новий клієнт потрапляє у чергу залежно від свого пріоритету. Зберігайте статистику запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LoginRequest:
    def __init__(self, login, password, priority):
        self.login = login
        self.password = password
        self.priority = priority
    def __str__(self):
        return f"Login: {self.login}, priority: {self.priority}"
class StatisticsQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def add_record(self, login, time):
        new_node = Node((login, time))
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def show(self):
        if self.is_empty():
            print("Statistics queue is empty")
            return
        current = self.head
        while current is not None:
            login, time = current.value
            print(f"Login: {login}, time: {time}")
            current = current.next
class ServerQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.statistics = StatisticsQueue()
    def is_empty(self):
        return self.head is None
    def add_request(self, request):
        new_node = Node(request)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        elif request.priority > self.head.value.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if request.priority > current.next.value.priority:
                    break
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        print("Request added")
    def process_request(self, time):
        if self.is_empty():
            print("Server queue is empty")
            return
        request = self.head.value
        self.head = self.head.next
        if self.is_empty():
            self.tail = None
        self.statistics.add_record(request.login, time)
        print(f"Request processed: {request.login}")
        return request
    def show_requests(self):
        if self.is_empty():
            print("Server queue is empty")
            return
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    def show_statistics(self):
        self.statistics.show()
server = ServerQueue()
server.add_request(LoginRequest("Bib", "bib123", 1))
server.add_request(LoginRequest("Bob", "bob123", 3))
server.add_request(LoginRequest("Bill", "bill123", 2))
print("\nRequests:")
server.show_requests()
print("\nProcessing:")
server.process_request("14:30")
server.process_request("14:31")
server.process_request("14:32")
print("\nStatistics:")
server.show_statistics()
# Завдання 2
# Створіть імітаційну модель «Причал морських катерів». Введіть таку інфор­мацію:
# Середній час між появою пасажирів на причалі у різний час доби;
# Середній час між появою катерів на причалі у різний час доби;
# Тип зупинки катера (кінцева або інша).
# Визначіть:
# Середній час перебування людини на зупинці;
# Достатній інтервал часу між приходами катерів, коли на зупинці не більше N людей одночасно;
# Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно.
import random
class Node:
    def __init__(self, time):
        self.time = time
        self.next = None
class PassengerQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def is_empty(self):
        return self.head is None
    def add_passenger(self, time):
        new_node = Node(time)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    def remove_passenger(self):
        if self.is_empty():
            return None
        time = self.head.time
        self.head = self.head.next
        if self.is_empty():
            self.tail = None
        self.count -= 1
        return time
    def size(self):
        return self.count
class Pier:
    def __init__(self, stop_type, max_seats, limit):
        self.stop_type = stop_type
        self.max_seats = max_seats
        self.limit = limit
        self.duration = 18 * 60
        self.passenger_intervals = [5, 3, 4]
        self.boat_intervals = [30, 20, 60]
        self.arrivals = []
        self.free_seats = []
    def get_period(self, time):
        if time < 360:
            return 0
        elif time < 720:
            return 1
        return 2
    def prepare_day(self):
        self.arrivals = []
        self.free_seats = []
        next_passenger = 0
        for time in range(self.duration):
            if time == next_passenger:
                self.arrivals.append(True)
                period = self.get_period(time)
                average = self.passenger_intervals[period]
                interval = random.randint(1, average * 2 - 1)
                next_passenger = time + interval
            else:
                self.arrivals.append(False)
            seats = random.randint(1, self.max_seats)
            if self.stop_type == "terminal":
                self.free_seats.append(seats)
            else:
                self.free_seats.append(random.randint(0, seats))
    def simulate(self, fixed_interval=None):
        queue = PassengerQueue()
        total_wait = 0
        served = 0
        max_people = 0
        if fixed_interval is None:
            next_boat = self.boat_intervals[0]
        else:
            next_boat = fixed_interval
        for time in range(self.duration):
            if self.arrivals[time]:
                queue.add_passenger(time)
            if queue.size() > max_people:
                max_people = queue.size()
            if time == next_boat:
                seats = self.free_seats[time]
                for i in range(seats):
                    if queue.is_empty():
                        break
                    arrival_time = queue.remove_passenger()
                    total_wait += time - arrival_time
                    served += 1
                if fixed_interval is None:
                    period = self.get_period(time)
                    next_boat = time + self.boat_intervals[period]
                else:
                    next_boat = time + fixed_interval
        if served > 0:
            average_wait = total_wait / served
        else:
            average_wait = None
        return average_wait, max_people, served, queue.size()
    def show_statistics(self):
        average, maximum, served, remaining = self.simulate()
        if self.stop_type == "terminal":
            print("Stop type: terminal")
        else:
            print("Stop type: intermediate")
        if average is None:
            print("No passengers boarded")
        else:
            print(f"Average waiting time of boarded passengers: {average:.2f} min")
        print("Maximum number of people in the queue:", maximum)
        print("Passengers boarded:", served)
        print("Passengers still waiting:", remaining)
    def find_interval(self, max_interval):
        for interval in range(max_interval, 0, -1):
            average, maximum, served, remaining = self.simulate(interval)
            if maximum <= self.limit:
                return interval
        return None
pier = Pier("terminal", 25, 25)
pier.prepare_day()
print("Statistics for the original schedule:")
pier.show_statistics()
interval = pier.find_interval(60)
print("\nInterval selection:")
if interval is None:
    print("No suitable interval found from 1 to 60 minutes")
else:
    print("Largest suitable interval:", interval, "min")
    print("Queue limit:", pier.limit)
    average, maximum, served, remaining = pier.simulate(interval)
    print("Maximum queue size with this interval:", maximum)
    if average is not None:
        print(f"Average waiting time of boarded passengers: {average:.2f} min")
    print("Passengers boarded:", served)
    print("Passengers still waiting:", remaining)

# Завдання 4
# Реалізуйте базу даних зі штрафами податкової інспекції. Ідентифікувати кожну конкретну людину буде персональний ідентифікаційний код. В однієї людини може бути багато штрафів.
# Реалізуйте:
# Повний друк бази даних;
# Друк даних за конкретним кодом;
# Друк даних за конкретним типом штрафу;
# Друк даних за конкретним містом;
# Додавання нової людини з інформацією про неї;
# Додавання нових штрафів для вже існуючого запису;
# Видалення штрафу;
# Заміна інформації про людину та її штрафи.
# Вибір необхідних структур даних визначте самостійно.
class Fine:
    def __init__(self, fine_type, amount):
        self.fine_type = fine_type
        self.amount = amount
    def __str__(self):
        return f"Type: {self.fine_type}, amount: {self.amount}"
class Person:
    def __init__(self, code, name, city):
        self.code = code
        self.name = name
        self.city = city
        self.fines = []
    def show_info(self):
        print(f"\nCode: {self.code}")
        print(f"Name: {self.name}")
        print(f"City: {self.city}")
    def show_fines(self):
        if not self.fines:
            print("No fines")
            return
        for i in range(len(self.fines)):
            print(f"{i + 1}. {self.fines[i]}")
    def show(self):
        self.show_info()
        self.show_fines()
class FineDatabase:
    def __init__(self):
        self.people = {}
    def add_person(self, code, name, city):
        if code in self.people:
            print("Person already exists")
            return
        self.people[code] = Person(code, name, city)
        print("Person added")
    def add_fine(self, code, fine_type, amount):
        if code not in self.people:
            print("Person not found")
            return
        if amount <= 0:
            print("Amount must be positive")
            return
        new_fine = Fine(fine_type, amount)
        self.people[code].fines.append(new_fine)
        print("Fine added")
    def show_all(self):
        if not self.people:
            print("Database is empty")
            return
        for person in self.people.values():
            person.show()
    def show_by_code(self, code):
        if code not in self.people:
            print("Person not found")
            return
        self.people[code].show()
    def show_by_type(self, fine_type):
        found = False
        for person in self.people.values():
            person_shown = False
            for fine in person.fines:
                if fine.fine_type == fine_type:
                    if not person_shown:
                        person.show_info()
                        person_shown = True
                    print(fine)
                    found = True
        if not found:
            print("Fines not found")
    def show_by_city(self, city):
        found = False
        for person in self.people.values():
            if person.city == city:
                person.show()
                found = True
        if not found:
            print("People not found")
    def remove_fine(self, code, number):
        if code not in self.people:
            print("Person not found")
            return
        fines = self.people[code].fines
        if number < 1 or number > len(fines):
            print("Invalid fine number")
            return
        fines.pop(number - 1)
        print("Fine deleted")
    def change_person(self, code, new_code, new_name, new_city):
        if code not in self.people:
            print("Person not found")
            return
        if new_code != code and new_code in self.people:
            print("Code already exists")
            return
        person = self.people.pop(code)
        person.code = new_code
        person.name = new_name
        person.city = new_city
        self.people[new_code] = person
        print("Person changed")
    def change_fine(self, code, number, new_type, new_amount):
        if code not in self.people:
            print("Person not found")
            return
        fines = self.people[code].fines
        if number < 1 or number > len(fines):
            print("Invalid fine number")
            return
        if new_amount <= 0:
            print("Amount must be positive")
            return
        fine = fines[number - 1]
        fine.fine_type = new_type
        fine.amount = new_amount
        print("Fine changed")
database = FineDatabase()
database.add_person("1111111111", "Bib", "Odesa")
database.add_person("2222222222", "Bob", "Kyiv")
database.add_person("3333333333", "Bill", "Odesa")
database.add_fine("1111111111", "Late tax payment", 1000)
database.add_fine("1111111111", "Late declaration", 500)
database.add_fine("2222222222", "Late tax payment", 1500)
database.add_fine("3333333333", "Late declaration", 700)
print("\nFull database:")
database.show_all()
print("\nSearch by code:")
database.show_by_code("1111111111")
print("\nSearch by fine type:")
database.show_by_type("Late tax payment")
print("\nSearch by city:")
database.show_by_city("Odesa")
print("\nChange person:")
database.change_person(
    "2222222222", "2222222222", "Bob Smith", "Lviv"
)
print("\nChange fine:")
database.change_fine(
    "1111111111", 1, "Late tax payment", 1200
)
print("\nDelete fine:")
database.remove_fine("1111111111", 2)
print("\nUpdated database:")
database.show_all()