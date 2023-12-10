import sqlite3 as sl

conn = sl.connect("test.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users
               (ID integer primary key,
               name text,
               surname text)
               ;""")

cursor.execute("INSERT INTO users VALUES (1, 'Ваня','Иванов');")

cursor.execute("SELECT * FROM users;")

print(cursor.fetchall())

