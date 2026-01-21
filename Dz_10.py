from bs4 import BeautifulSoup
import requests
import datetime
import sqlite3

current_time = datetime.datetime.now()
current_date_time = current_time.strftime("%d.%m.%Y %H:%M:%S")

response = requests.get("https://sinoptik.ua/pohoda/chernihiv")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    soup_list = soup.find("p", {"class": "R1ENpvZz"})
    temperature = soup_list.text




connection = sqlite3.connect("Dz_DB.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS info_temp (date TEXT, temp TEXT);")
cur.execute("INSERT INTO info_temp (date, temp) VALUES (?, ?);", (current_date_time, temperature))
cur.execute("SELECT * FROM info_temp")
rows = cur.fetchall()
for row in rows:
    print(f"Дата: {row[0]} | Температура: {row[1]}")
connection.commit()
connection.close()