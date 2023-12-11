import sqlite3
from os import path

absPath = path.join(path.dirname(path.dirname(__file__)), "base.db")


connection = sqlite3.connect(absPath)
cursor = connection.cursor()

cursor.execute('''CREATE TABLE products (id INTEGER PRIMARY KEY, title TEXT, price REAL, desc TEXT, image TEXT)''')
cursor.execute(''' 
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        login TEXT UNIQUE,
        password TEXT,
        admin INTEGER
    )      
''')

dataProducts = [
    (1, "Солнцезащитные очки", 300.00, "Защищают от солнца", "/static/image/glasses1.png"),
    (2, "Медицинские очки", 4000.00, "Улучшают зрение", "/static/image/glasses2.png"),
    (3, "Плавательные очки", 800.00, "Помогают плавать в воде с открытыми глазами", "/static/image/glasses3.png")
]

# 0 - обычный клиент
# 1 - сотрудник сайта
# 2 - главный менеджер

dataUsers = [
    (1, "Олег Корпатович", "123456789", 1),
    (2, "Владимир Центральный", "admin", 2)
]

cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?)", dataProducts)
cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", dataUsers)
connection.commit()

connection.close()