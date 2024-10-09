import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Отримання введення користувача
user_input = input("Введите название сервера для поиска: \n")

# Запит рядка з бази даних, який відповідає введеному значенню
cursor.execute("SELECT * FROM server_data WHERE server_name = ?", (user_input,))
row = cursor.fetchone()

# Закриття з'єднання
conn.close()

# Показ результату
if row:
    print(f"Найденный сервер: {row}")
else:
    print("Сервер не найден")
