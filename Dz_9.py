import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, usd):
        self.rate = float(usd.replace(',', '.'))
    def convert(self, amount_uah):
        return amount_uah / self.rate

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    usd_cell = soup.find("td", string="USD")

    if usd_cell:
        row = usd_cell.find_parent("tr")
        cells = row.find_all("td")
        usd_text = cells[4].text.strip()

        print(f"1 USD = {usd_text} UAH")
        converter = CurrencyConverter(usd_text)

        uah_amount = float(input("Введіть кількість гривень: "))
        result = converter.convert(uah_amount)
        print(f"Сума в доларах США: {result:.2f} USD")

    else:
        print("Не вдалося знайти курс доллару")
else:
    print("Нема доступу")