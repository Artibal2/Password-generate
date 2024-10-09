import random
import sqlite3

# Підключення до бази даних або створення нової, якщо її ще немає
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Створення таблиці, якщо її ще немає
cursor.execute('CREATE TABLE IF NOT EXISTS server_data\n'
               '                  (id INTEGER PRIMARY KEY, server_name TEXT, random_text TEXT)')

aname = input("Введите название сервера \n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = [("A"), ("B"), ("C"), ("D"), ("E"), ("F"), ("G"), ("H"), ("I"), ("J"), ("K"), ("L"), ("M"), ("N"), ("O"), ("P"), ("Q"), ("R"), ("S"), ("T"), ("U"), ("V"), ("W"), ("X"), ("Y"), ("Z"), "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Приведення всіх елементів до рядкового типу
all_characters = [str(x) for x in numbers + letters]

# Генерація випадкового тексту до 10 символів
random_text = ''.join(random.choice(all_characters) for _ in range(10))
print(random_text)

# Додавання даних у базу даних
cursor.execute("INSERT INTO server_data (server_name, password) VALUES (?, ?)", (aname, random_text))

# Збереження змін
conn.commit()

# Закриття з'єднання
conn.close()
