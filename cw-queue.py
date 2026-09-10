# class BankQueue:
#     def __init__(self):
#         self.clients = []
#
#     def add_client(self, client):
#         self.clients.append(client)
#
#     def remove_client(self):
#         if self.is_empty():
#             return None
#         return self.clients.pop(0)
#
#     def is_empty(self):
#         return len(self.clients) == 0
#
#     def size(self):
#         return len(self.clients)
#
#     def next_client(self):
#         if self.is_empty():
#             return None
#         return self.clients[0]
#
#     def show_client(self):
#         if self.is_empty():
#             print("Empty bank Queue")
#         else:
#             for client in self.clients:
#                 print(client)
#
#
# bank = BankQueue()
#
# bank.add_client("client 1")
# bank.add_client("client 2")
# bank.add_client("client 3")
#
# bank.show_client()
#
# print(bank.remove_client())
# print("===========after del ===============")
# bank.show_client()
#
# print(bank.next_client())
#
# class PrinterQueue:
#     def __init__(self):
#         self.jobs = []
#
#     def add_job(self, job):
#         self.jobs.append(job)
#
#     def print_next(self):
#         if self.is_empty():
#             print("Empty queue")
#             return None
#         return self.jobs.pop(0)
#
#     def is_empty(self):
#         return len(self.jobs) == 0
#
#     def show_jobs(self):
#         if self.is_empty():
#             print("Empty job Queue")
#         else:
#             for job in self.jobs:
#                 print(job)
#
# job_queue = PrinterQueue()
#
# job_queue.add_job("doc 1")
# job_queue.add_job("doc 2")
# job_queue.add_job("doc 3")
# job_queue.show_jobs()
#
# print("===========after printing===========")
# print(job_queue.print_next())
#
# job_queue.show_jobs()

# class PrintJob:
#     def __init__(self, document,pages,priority):
#         self.document=document
#         self.pages=pages
#         self.priority=priority
#
#     def __str__(self):
#         return f"{self.document}, {self.pages}, {self.priority}"
#
# class PrinterQueue:
#     def __init__(self):
#         self.jobs = []
#
#     def add_job(self, job):
#         if isinstance(job,PrintJob):
#             self.jobs.append(job)
#
#
#     def print_next(self):
#         if self.is_empty():
#             print("Empty queue")
#             return
#         highest_priority = 0
#
#         for i in range(1,len(self.jobs)):
#             if self.jobs[i].priority > self.jobs[highest_priority].priority:
#                 highest_priority = i
#         return self.jobs.pop(highest_priority)
#
#
#     def is_empty(self):
#         return len(self.jobs) == 0
#
#     def show_jobs(self):
#         #         return value
# #
# #     def show(self):
# #         if self.is_empty():
# #             print("queue is empty")
# #             return
# #         index = self.front
# #
# #         for i in range(self.count):
# #             print(self.queue[index])
# #             index = (index + 1) % self.maxsize
# #
# #
# # queue = CircularQueue(5)
# # queue.enqueue(1)
# # queue.enqueue(2)
# # queue.enqueue(3)
# #
# # print("queue:")
# # queue.show()
# #
# # print("dequeue")
# # print(queue.dequeue())
# # print(queue.dequeue())
# #
# # print("queue:")
# # queue.show()
# #
# # queue.enqueue(4)
# # queue.enqueue(5)
# # queue.enqueue(6)
# # queue.enqueue(7)
# # queue.enqueue(8)
# #
# # queue.show()
#
#
# class Deque:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return self.items == []
#
#     def add_front(self, item):
#         self.items.insert(0, item)
#
#     def add_back(self, item):
#         self.items.append(item)
#
#     def remove_front(self):
#         if self.is_empty():
#             print('Deque is empty')
#             return
#         return self.items.pop(0)
#
#     def remove_back(self):
#         if self.is_empty():
#             print('Deque is empty')
#             return
#         return self.items.pop()
#
#
#     def show(self):
#         print(self.items)
#
# deque = Deque()
# deque.add_back("Client 1")
# deque.add_back("Client 2")
# deque.add_front("vip client")
# deque.remove_front()
# deque.show()

#
# Завдання 1
# Розробіть додаток, який дозволяє зберігати інформацію
# про логіни і паролі користувачів. Кожному користувачеві
# відповідає пара «логін ­— пароль». При старті додатку
# відображається меню:
# Додати нового користувача;
# Видалити існуючого користувача;
# Перевірити, чи існує такий користувач;
# Змінити логін існуючого користувача;
# Змінити пароль існуючого користувача.
# Для реалізації завдання обов('язково застосуйте одну із '
# структур даних. При виборі структури керуйтеся постановкою
# завдання.)

class Node:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.next = None
class UserList:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def user_exists(self, login):
        current = self.head
        while current is not None:
            if current.login == login:
                return True
            current = current.next
        return False
    def add_user(self, login, password):
        if self.user_exists(login):
            print("User already exists")
            return
        new_user = Node(login, password)
        if self.is_empty():
            self.head = new_user
            self.tail = new_user
        else:
            self.tail.next = new_user
            self.tail = new_user
        print("User added")
    def remove_user(self, login):
        current = self.head
        previous = None
        while current is not None:
            if current.login == login:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current is self.tail:
                    self.tail = previous
                print("User deleted")
                return
            previous = current
            current = current.next
        print("User not found")
    def change_login(self, old_login, new_login):
        if not self.user_exists(old_login):
            print("User not found")
            return
        if self.user_exists(new_login):
            print("Login already exists")
            return
        current = self.head
        while current is not None:
            if current.login == old_login:
                current.login = new_login
                print("Login changed")
                return
            current = current.next
    def change_password(self, login, new_password):
        current = self.head
        while current is not None:
            if current.login == login:
                current.password = new_password
                print("Password changed")
                return
            current = current.next
        print("User not found")


users = UserList()

while True:
    print("\n1. Add user")
    print("2. Delete user")
    print("3. Check user")
    print("4. Change login")
    print("5. Change password")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        login = input("Enter login: ")
        password = input("Enter password: ")
        users.add_user(login, password)

    elif choice == "2":
        login = input("Enter login: ")
        users.remove_user(login)

    elif choice == "3":
        login = input("Enter login: ")

        if users.user_exists(login):
            print("User exists")
        else:
            print("User not found")

    elif choice == "4":
        old_login = input("Enter old login: ")
        new_login = input("Enter new login: ")
        users.change_login(old_login, new_login)

    elif choice == "5":
        login = input("Enter login: ")
        new_password = input("Enter new password: ")
        users.change_password(login, new_password)

    elif choice == "0":
        break

    else:
        print("Invalid choice")