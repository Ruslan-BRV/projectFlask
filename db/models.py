import sqlite3

def getALLProducts():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()

    connection.close()

    return result

def getSomeProducts(min, max):
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM products WHERE ? <= price AND price <=?", (min, max))
    result = cursor.fetchall()

    connection.close()

    return result

def getUser(login, password):
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute(''' 
        SELECT * 
        FROM users
        WHERE login = ? AND password = ? 
    ''', (login, password))
    result = cursor.fetchone()
    connection.close()
    return result

def addProduct(idProduct, title, price, desc, pathPhoto):
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO products
        VALUES (?, ?, ?, ?, ?)
    ''', (idProduct, title, price, desc, pathPhoto))

    connection.commit()

    connection.close()

def deleteProduct(idProduct):
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (idProduct,))

    connection.commit()

    connection.close()