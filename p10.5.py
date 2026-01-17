import sqlite3

connection = sqlite3.connect("pet_DB.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE info_pet (name TEXT, type TEXT, age INTEGER);")
connection.commit()
connection.close()