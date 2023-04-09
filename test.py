import requests
text = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").text
print(text)