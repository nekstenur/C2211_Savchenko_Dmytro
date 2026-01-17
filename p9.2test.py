import requests
responce = requests.get('https://www.roblox.com/home')
print(responce.text)