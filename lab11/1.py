import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="lab11",  
    user="postgres",  
    password="sanzhar_00",  
    host="localhost"
)


cur = conn.cursor()

# 1. Функция поиска записей по паттерну
def search_phonebook(pattern):
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


search_phonebook('John')

# 2. Процедура вставки или обновления пользователя
def insert_or_update_user(first_name, last_name, phone_number):
    cur.execute("CALL insert_or_update_user(%s, %s, %s);", 
                (first_name, last_name, phone_number))
    conn.commit()


insert_or_update_user('John', 'Doe', '1234567890')

# 3. Процедура вставки нескольких пользователей
def insert_multiple_users(users):
    for user in users:
        first_name, last_name, phone_number = user
        cur.execute("CALL insert_or_update_user(%s, %s, %s);", 
                    (first_name, last_name, phone_number))
    conn.commit()


users = [
    ('John', 'Doe', '1234567890'),
    ('Jane', 'Doe', '9876543210')
]
insert_multiple_users(users)

# 4. Функция с пагинацией
def get_phonebook_paginated(limit, offset):
    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)


get_phonebook_paginated(10, 0)

# 5. Процедура для удаления по имени пользователя или телефону
def delete_user_by_username_or_phone(first_name=None, last_name=None, phone_number=None):
    cur.execute("CALL delete_user_by_username_or_phone(%s, %s, %s);", 
                (first_name, last_name, phone_number))
    conn.commit()


delete_user_by_username_or_phone('John', 'Doe')  # Удаление по имени
delete_user_by_username_or_phone(None, None, '1234567890')  # Удаление по телефону

# Закрытие соединения
cur.close()
conn.close()
