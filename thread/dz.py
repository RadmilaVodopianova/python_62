# Завдання 1. Два паралельні лічильники
# Створіть дві функції:
# перша виводить числа від 1 до 10;
# друга виводить числа від 10 до 1.
# Запустіть кожну функцію в окремому потоці.
# Між виведенням чисел зробіть невелику затримку:
# time.sleep(0.5)
# Програма повинна дочекатися завершення обох потоків.
# Обов'язково використати: Thread, start(), join().
import threading
import time
import random
def count_up():
    for number in range(1, 11):
        print(f"Перший потік: {number}")
        time.sleep(0.5)

def count_down():
    for number in range(10, 0, -1):
        print(f"Другий потік: {number}")
        time.sleep(0.5)

t1 = threading.Thread(target=count_up)
t2 = threading.Thread(target=count_down)

t1.start()
t2.start()

t1.join()
t2.join()
# Завдання 2. Завантаження файлів
# Уявіть, що програма одночасно завантажує три файли:
# photo.jpg
# video.mp4
# document.pdf
# Для кожного файлу створіть окремий потік.
# Функція повинна отримувати назву файлу та виводити:
# Початок завантаження photo.jpg
# ...
# photo.jpg завантажено
# Для імітації завантаження використайте:
# time.sleep()
# Для різних файлів встановіть різний час завантаження.
# Наприкінці, після завершення всіх потоків, програма повинна вивести:
# Усі файли завантажено!
def download_file(filename, seconds):
    print(f"Початок завантаження {filename}")
    time.sleep(seconds)
    print(f"{filename} завантажено")

t1 = threading.Thread(target=download_file, args=("photo.jpg", 2))
t2 = threading.Thread(target=download_file, args=("video.mp4", 4))
t3 = threading.Thread(target=download_file, args=("document.pdf", 3))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Усі файли завантажено!")
# Завдання 3. Гонка спортсменів
# Створіть функцію:
# def runner(name):
#     ...
# Кожен спортсмен повинен пройти 5 етапів.
# Наприклад:
# Олег пройшов етап 1
# Анна пройшла етап 1
# Олег пройшов етап 2
# Максим пройшов етап 1
# ...
# Анна фінішувала!
# Створіть 3 потоки для трьох спортсменів.
# Час проходження кожного етапу повинен бути випадковим:
# random.uniform(0.5, 1.5)
# Подумайте, чому спортсмени фінішують у різному порядку.
def runner(name):
    for stage in range(1, 6):
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{name}: етап {stage} пройдено")
    print(f"{name}: фініш!")


t1 = threading.Thread(target=runner, args=("Олег",))
t2 = threading.Thread(target=runner, args=("Анна",))
t3 = threading.Thread(target=runner, args=("Максим",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# Завдання 6. Мініпроєкт «Служба доставки»
# Є декілька кур'єрів:
# Courier 1
# Courier 2
# Courier 3
# Кожен кур'єр отримує окреме замовлення і проходить три етапи:
# Courier 1: отримав замовлення
# Courier 1: забрав замовлення
# Courier 1: їде до клієнта
# Courier 1: замовлення доставлено
# Кожен етап займає випадковий час.
# Кожен кур'єр працює в окремому потоці, тому повідомлення різних кур'єрів повинні перемішуватися.
# Після завершення всіх потоків:
# === УСІ ЗАМОВЛЕННЯ ДОСТАВЛЕНО ===
# Додаткове завдання: порахуйте час виконання всієї програми за допомогою:
# time.time()
# Після цього запустіть ті самі доставки без потоків і порівняйте час.
# Остання частина тут особливо корисна: вони не просто використають Thread, а на практиці побачать, навіщо
# потрібна багатопотоковість для задач з очікуванням.

def delivery(name, delays):
    print(f"{name}: отримав замовлення")
    time.sleep(delays[0])

    print(f"{name}: забрав замовлення")
    time.sleep(delays[1])

    print(f"{name}: їде до клієнта")
    time.sleep(delays[2])

    print(f"{name}: замовлення доставлено")

def compare_delivery_time(couriers):
    print("\nДоставка з потоками:")
    start_time = time.time()

    threads = []

    for name, delays in couriers:
        thread = threading.Thread(target=delivery, args=(name, delays))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    parallel_time = time.time() - start_time
    print("=== УСІ ЗАМОВЛЕННЯ ДОСТАВЛЕНО ===")

    print("\nДоставка без потоків:")
    start_time = time.time()

    for name, delays in couriers:
        delivery(name, delays)

    sequential_time = time.time() - start_time
    print("=== УСІ ЗАМОВЛЕННЯ ДОСТАВЛЕНО ===")

    print(f"\nЧас із потоками: {parallel_time:.2f} с")
    print(f"Час без потоків: {sequential_time:.2f} с")

print("\nЗавдання 6")

couriers = []

for number in range(1, 4):
    delays = [random.uniform(0.5, 1.5) for _ in range(3)]
    couriers.append((f"Courier {number}", delays))

compare_delivery_time(couriers)