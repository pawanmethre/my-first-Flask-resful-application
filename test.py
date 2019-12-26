import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text )"
cursor.execute(create_table)
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)
users = [(2, 'rolf', 'asdf'), (3, 'anne', 'xyz')]
cursor.executemany(insert_query, users)
select_rows = "SELECT * FROM users"
rows = cursor.execute(select_rows)

for row in rows:
    print(row)

connection.commit()
connection.close()
