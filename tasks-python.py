def is_palindrome():
    str = input("Введите строку: ")
    str = str.replace(" ", "").lower()
    if (str == str[::-1]):
        print("Да, это палиндром")
    else:
        print("Нет, это не палиндром")
        print(str[::-1])

def find_min_elements():
    matrix = []
    while True:
        line = input("Введите строку матрицы (или 'end' для завершения ввода): ")
        if line == 'end':
            break
        row = [int(num) for num in line.split()]
        matrix.append(row)
    i = 0

    for row in matrix:
        print(row)
        print(f"Минимальное значение в строке {i + 1}: {min(row)}")

def persons():

    word_count = {}
    text = input().lower()
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word, count in word_count.items():
        print(f"{word}: {count}")

import mysql

def connect_to_mysql():
    try:
        # Замените параметры подключения на свои
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='pass',
            database='my_db'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к базе данных: {err}")
        return None

def query_users_by_birth_year(connection, year):
    if connection is not None:
        cursor = connection.cursor()
        query = "SELECT first_name, last_name, date_of_birth FROM user WHERE YEAR(date_of_birth) = %s"
        cursor.execute(query, (year,))

        for (first_name, last_name, date_of_birth) in cursor:
            print(f"{first_name} {last_name} ({date_of_birth})")

        cursor.close()
    else:
        print("Соединение с базой данных не установлено.")


if __name__ == "__main__":
    year = input("Введите год рождения для поиска: ")
    try:
        year = int(year)
    except ValueError:
        print("Неверный формат года.")
        exit()

    db_connection = connect_to_mysql()

    if db_connection:
        query_users_by_birth_year(db_connection, year)
        db_connection.close()