import sqlite3 as db

conn = db.connect('test.db')

cursor = conn.cursor()
cursor.execute("CREATE TABLE Films(Title Text, Director Text, Year Text)")

conn.close()

print("conection closed\ndatabase created")

