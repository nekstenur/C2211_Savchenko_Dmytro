import requests
responce = requests.get('https://httpbin.org/get')
print(responce.text)