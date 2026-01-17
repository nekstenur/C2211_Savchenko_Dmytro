import sqlite3

connection = sqlite3.connect("pet_DB.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name, age FROM info_pet WHERE age > 5;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()