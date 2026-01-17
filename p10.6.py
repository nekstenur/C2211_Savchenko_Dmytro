import sqlite3

connection = sqlite3.connect("pet_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO info_pet (name, type, age) VALUES ('Kesha', 'parrot', 4);")
cur.execute("INSERT INTO info_pet (name, type, age) VALUES ('Istorichka', 'devil', 80);")
cur.execute("INSERT INTO info_pet (name, type, age) VALUES ('Vasya', 'cat', 12);")
cur.execute("INSERT INTO info_pet (name, type, age) VALUES ('Tysa', 'fish', 1);")
connection.commit()
connection.close()