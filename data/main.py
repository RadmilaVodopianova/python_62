import sqlite3
from contextlib import closing
from pathlib import Path

folder = Path(__file__).resolve().parent

# Завдання 1: оцінки студентів.
with closing(sqlite3.connect(folder / "students.db")) as conn:
    conn.executescript('''
    DROP TABLE IF EXISTS "Оцінки студентів";

    CREATE TABLE "Оцінки студентів" (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        "ПІБ студента" TEXT NOT NULL,
        "Місто" TEXT NOT NULL,
        "Країна" TEXT NOT NULL,
        "Дата народження" TEXT NOT NULL,
        "Електронна адреса" TEXT NOT NULL,
        "Контактний телефон" TEXT NOT NULL,
        "Назва групи" TEXT NOT NULL,
        "Середня оцінка за рік" REAL NOT NULL,
        "Предмет з мінімальною середньою оцінкою" TEXT NOT NULL,
        "Предмет з максимальною середньою оцінкою" TEXT NOT NULL
    );
    ''')
    conn.commit()
print('students.db: таблицю "Оцінки студентів" створено.')

# Завдання 2: лікарня.
with closing(sqlite3.connect(folder / "Hospital.db")) as conn:
    conn.executescript('''
    DROP TABLE IF EXISTS Departments;
    DROP TABLE IF EXISTS Diseases;
    DROP TABLE IF EXISTS Doctors;
    DROP TABLE IF EXISTS Examinations;
    DROP TABLE IF EXISTS Wards;

    CREATE TABLE Departments (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Building INTEGER NOT NULL
            CHECK (Building BETWEEN 1 AND 5),
        Financing REAL NOT NULL DEFAULT 0
            CHECK (Financing >= 0),
        Name TEXT NOT NULL UNIQUE
            CHECK (length(trim(Name)) > 0 AND length(Name) <= 100)
    );

    CREATE TABLE Diseases (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL UNIQUE
            CHECK (length(trim(Name)) > 0 AND length(Name) <= 100),
        Severity INTEGER NOT NULL DEFAULT 1
            CHECK (Severity >= 1)
    );

    CREATE TABLE Doctors (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
            CHECK (length(trim(Name)) > 0),
        Phone TEXT
            CHECK (Phone IS NULL
                   OR (length(Phone) = 10 AND Phone NOT GLOB '*[^0-9]*')),
        Salary REAL NOT NULL
            CHECK (Salary > 0),
        Surname TEXT NOT NULL
            CHECK (length(trim(Surname)) > 0)
    );

    CREATE TABLE Examinations (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        DayOfWeek INTEGER NOT NULL
            CHECK (DayOfWeek BETWEEN 1 AND 7),
        EndTime TEXT NOT NULL
            CHECK (EndTime GLOB '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]'),
        Name TEXT NOT NULL UNIQUE
            CHECK (length(trim(Name)) > 0 AND length(Name) <= 100),
        StartTime TEXT NOT NULL
            CHECK (StartTime GLOB '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]'
                   AND StartTime BETWEEN '08:00:00' AND '18:00:00'),
        CHECK (EndTime > StartTime)
    );

    CREATE TABLE Wards (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Building INTEGER NOT NULL
            CHECK (Building BETWEEN 1 AND 5),
        Floor INTEGER NOT NULL
            CHECK (Floor >= 1),
        Name TEXT NOT NULL UNIQUE
            CHECK (length(trim(Name)) > 0 AND length(Name) <= 20)
    );
    ''')
    conn.commit()

    tables = conn.execute('''
        SELECT name FROM sqlite_master
        WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    ''').fetchall()

print("Hospital.db: створено таблиці:")
for table in tables:
    print("-", table[0])
