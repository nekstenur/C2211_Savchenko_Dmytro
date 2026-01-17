import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for item in response_parse:
    if item.startswith("$"):
        for item_2 in item.split("</span>"):
            if item.startswith("$") and item_2[1].isdigit():
                res_parse_list.append(item_2)

bitcoin_price = res_parse_list[6]
print(bitcoin_price)