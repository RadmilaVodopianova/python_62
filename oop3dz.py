# 1)Потрібно створити клас "Фільм", в якому використовуватиметься клас-метод з ім'ям "середній_рейтинг",
# який буде обчислювати середній рейтинг всіх фільмів, створених з використанням цього класу.
# реалізуйте функцію для виведення рейтингу всіх фільмів та функцію для виведення імен.
class Film:
    films = []
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        Film.films.append(self)
    @classmethod
    def average_rating(cls):
        total = sum(film.rating for film in cls.films)
        return total / len(cls.films)
    @classmethod
    def show_ratings(cls):
        for film in cls.films:
            print(f"{film.name}: {film.rating}")
    @classmethod
    def show_names(cls):
        for film in cls.films:
            print(film.name)
film1 = Film("Spider-Man: Homecoming", 7.4)
film2 = Film("Spider-Man: Far From Home", 7.4)
film3 = Film("Spider-Man: No Way Home", 8.2)
print("Названия фильмов:")
Film.show_names()
print("\nРейтинги фильмов:")
Film.show_ratings()
print("\nСредний рейтинг:")
print(Film.average_rating())
# 2)Використовуючи механізм множинного успадкування, розробіть клас "Людина". Мають бути класи "Мозок", "Серце", "Ноги" і т.д.
class Brain:
    def think(self):
        print("Мозг думает")
class Heart:
    def beat(self):
        print("Сердце бьется")
class Legs:
    def walk(self):
        print("Ноги ходят")
class Lungs:
    def breathe(self):
        print("Легкие дышат")
class Human(Brain, Heart, Legs, Lungs):
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"Человек: {self.name}")
person = Human("Peter Parker")
person.show_info()
person.think()
person.beat()
person.walk()
person.breathe()
# 3)
# 1 Створіть базовий клас Instrument, який представлятиме загальні властивості та методи для всіх музичних інструментів.
# Визначте метод play, який має бути реалізований у підкласах.
# 2 Створіть підкласи StringInstrument, WindInstrument і PercussionInstrument, які представляють струнні, духові та ударні інструменти відповідно.
# Кожен із цих класів повинен успадковувати від Instrument та надавати свою реалізацію методу play.
# 3 Створіть додаткові підкласи для конкретних музичних інструментів, таких як Guitar, Flute та Drum.
# Ці класи повинні успадковувати від відповідних підкласів (StringInstrument, WindInstrument, або PercussionInstrument) та
# можуть додатково визначати свої унікальні методи та властивості, наприклад, метод tune для налаштування гітари.
# 4 Створіть екземпляри різних музичних інструментів та викличте метод play для кожного з них, щоб побачити,
# як кожний інструмент звучить.
# 5 Реалізуйте множинне спадкування, щоб створити новий клас HybridInstrument, який успадковує від кількох класів,
# які представляють різні види музичних інструментів. У цьому класі визначте свій метод play, що комбінує звуки від усіх успадкованих класів.
# 6 Створіть екземпляр HybridInstrument і викличте його метод play, щоб побачити, як множинне успадкування дозволяє комбінувати властивості та методи з кількох батьківських класів
# 3. Музичні інструменти

class Instrument:
    def __init__(self, name):
        self.name = name
    def play(self):
        raise NotImplementedError("Метод play должен быть реализован")
class StringInstrument(Instrument):
    def play(self):
        print(f"{self.name}: звучит струна")
class WindInstrument(Instrument):
    def play(self):
        print(f"{self.name}: звучит духовой инструмент")
class PercussionInstrument(Instrument):
    def play(self):
        print(f"{self.name}: звучит ударный инструмент")
class Guitar(StringInstrument):
    def tune(self):
        print(f"{self.name}: гитара настроена")
class Flute(WindInstrument):
    def clean(self):
        print(f"{self.name}: флейта очищена")
class Drum(PercussionInstrument):
    def hit(self):
        print(f"{self.name}: удар по барабану")
class Piano(Instrument):
    def play(self):
        print(f"{self.name}: звучат клавиши")

    def press_key(self):
        print(f"{self.name}: нажата клавиша")
guitar = Guitar("Гитара")
flute = Flute("Флейта")
drum = Drum("Барабан")
piano = Piano("Фортепиано")
guitar.play()
flute.play()
drum.play()
piano.play()
guitar.tune()
flute.clean()
drum.hit()
piano.press_key()
class HybridInstrument(Guitar, Drum, Piano):
    def play(self):
        Guitar.play(self)
        Drum.play(self)
        Piano.play(self)
hybrid = HybridInstrument("Гибридный инструмент")
hybrid.play()