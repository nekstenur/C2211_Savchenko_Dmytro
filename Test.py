from bs4 import BeautifulSoup
import requests

response = requests.get("https://store.steampowered.com/charts/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    soup_list = soup.find("div", {"class": "TY7Qbq7FuibkQDpXGPxsj"})
    print(soup_list)
else:
    print("Bye, bye!")