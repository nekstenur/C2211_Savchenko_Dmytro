import random
import time
import datetime
import sys
import requests
import sqlite3
from bs4 import BeautifulSoup


def save_to_db(date, card, uah, paper):
    connection = sqlite3.connect("Bank_HistoryDB.sl3")
    cur = connection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS receipts 
                   (date TEXT, card_num TEXT, card_balance REAL, pocket_money REAL);""")
    cur.execute("INSERT INTO receipts VALUES (?, ?, ?, ?);", (date, card, uah, paper))
    connection.commit()
    connection.close()


def show_history():
    secret_code = input("Введіть код доступу: ")
    if secret_code == "8906":
        try:
            connection = sqlite3.connect("Bank_HistoryDB.sl3")
            cur = connection.cursor()
            cur.execute("SELECT * FROM receipts")
            rows = cur.fetchall()

            if not rows:
                print("База даних порожня.")
            else:
                print("\n--- ІСТОРІЯ ОПЕРАЦІЙ ---")
                for row in rows:
                    print(f"Дата: {row[0]} | Карта: {row[1]} | Баланс: {row[2]} | Готівка: {row[3]}")
                print("-----------------------")
            connection.close()
        except sqlite3.OperationalError:
            print("Базу даних ще не створено.")
    else:
        print("Невірний код! Доступ заборонено.")


class CurrencyConverter:
    def __init__(self, usd_rate_str):
        self.rate = float(usd_rate_str.replace(',', '.'))

    def convert(self, amount_uah):
        return amount_uah / self.rate


def show_exchange_rates():
    print("Шукаю актуальні курси валют...")
    try:
        response = requests.get("https://bank.gov.ua/ua/markets/exchangerates", timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            curs = ["USD", "EUR", "PLN"]
            print("\nПоточний курс валют (НБУ):")
            print("-" * 30)

            for code in curs:
                cell = soup.find("td", string=code)
                if cell:
                    row = cell.find_parent("tr")
                    rate_val = row.find_all("td")[4].text.strip()
                    print(f"1 {code} = {rate_val} грн")
            print("-" * 30)
            return True
    except:
        return None
    return None


def print_balance(card, paper, card_num):
    print("\n" + "=" * 40)
    print(f" Готівка: {paper} грн | На картці: {card} грн")
    print(f" Картка: {card_num}")
    print("=" * 40)


def handle_transaction(paper, card, mode):
    try:
        if mode == "deposit":
            amount = int(input("Скільки кладемо на карту? "))
            if 0 < amount <= paper:
                print("Рахую гроші...")
                time.sleep(2)
                return paper - amount, card + amount
            print("У вас стільки немає.")

        elif mode == "withdraw":
            amount = int(input("Скільки зняти? "))
            if 0 < amount <= card:
                print("Видаю купюри...")
                time.sleep(2)
                return paper + amount, card - amount
            print("Мало грошей на карті.")
    except ValueError:
        print("Пишіть тільки цифри.")
    return paper, card


def save_receipt(paper, card, card_num):
    now_obj = datetime.datetime.now()
    now_str = now_obj.strftime('%Y-%m-%d %H:%M:%S')
    file_name = f"receipt_{now_obj.strftime('%H%M%S')}.txt"

    receipt_text = f"Дата: {now_str}\nКарта: {card_num}\nНа карті: {card}\nГотівка: {paper}"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(receipt_text)

    save_to_db(now_str, card_num, card, paper)
    print(f"Готово! Чек записано у файл {file_name} та збережено в базу.")


print("--- ВАС ВІТАЄ БАНКОМАТ ---")
try:
    money_paper = int(input("Скільки у вас грошей в кишені?: "))
except:
    money_paper = 0

card_num = input("Номер вашої картки: ")
card_pin = input("Ваш пін-код: ")

if len(card_num) < 4 or len(card_pin) != 4:
    print("Помилка в даних.")
    sys.exit()

money_card = 0
print_balance(money_card, money_paper, card_num)

if input("Введіть пін: ") != card_pin:
    print("Невірно. Крадіжка!.")
    sys.exit()

while True:
    print("\nЩо будемо робити?")
    print("1. Покласти гроші")
    print("2. Зняти гроші")
    print("3. Перевірити курс валют")
    print("4. Баланс")
    print("5. Зробити чек")
    print("6. Піти геть")
    print("0. (Секретно) Переглянути базу даних")

    choice = input("Ваш вибір: ")

    if choice == "1":
        money_paper, money_card = handle_transaction(money_paper, money_card, "deposit")
    elif choice == "2":
        money_paper, money_card = handle_transaction(money_paper, money_card, "withdraw")
    elif choice == "3":
        if not show_exchange_rates():
            print("Нема зв'язку з банком.")
    elif choice == "4":
        print_balance(money_card, money_paper, card_num)
    elif choice == "5":
        save_receipt(money_paper, money_card, card_num)
    elif choice == "6":
        print("Бувай!")
        break
    elif choice == "0":
        show_history()
    else:
        print("Нема такого пункту.")