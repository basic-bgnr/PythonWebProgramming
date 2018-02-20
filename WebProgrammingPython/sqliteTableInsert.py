import sqlite3 as db

conn = db.connect('test.db')

cursor = conn.cursor()

cursor.execute('INSERT INTO Films VALUES("The GodFather", "Francis ford Coppola", "1987")')
cursor.execute('INSERT INTO Films VALUES("The GodFather", "Jeremy Renners", "1976")')
cursor.execute('INSERT INTO Films VALUES("The magician", "Henri Fonda", "1978")')

cursor.close()

conn.commit()
conn.close()
print('database inserted')
