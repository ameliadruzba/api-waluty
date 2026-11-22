import requests
import csv

dane = requests.get('https://api.nbp.pl/api/exchangerates/tables/C?format=json')

data = dane.json()

with open('dane.csv', 'w', newline=';', encoding='utf-8') as file:
    naglowki = ["currency", "code", "bid", "ask"]
    writer =  csv.DictWriter(file, fieldnames=naglowki)

    writer.writeheader()

    for kurs in data[0]["rates"]:
        writer.writerow({
            "currency": kurs["currency"],
            "code": kurs["code"],
            "bid": kurs["bid"],
            "ask": kurs["ask"]
        })

