import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
create_table_items = "CREATE TABLE items(name TEXT, price REAL)"
cursor.execute(create_table)
cursor.execute(create_table_items)

connection.commit()
connection.close()

