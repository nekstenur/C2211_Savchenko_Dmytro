import sqlite3

connection = sqlite3.connect("ItStep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT * FROM  first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()