from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    soup_list = soup.find_all("div", {"class": "sc-631098c-0"})
    for item in soup_list:
        print(item.text)