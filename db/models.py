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

