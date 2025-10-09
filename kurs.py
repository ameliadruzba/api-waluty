import csv

waluta = input('podaj walute na jaka chcesz przeliczyc: ').upper()
kwota = float(input('Podaj kwote jaka chcesz przeliczyc(zl): '))

with open('dane.csv', 'r') as file:
    reader = csv.DictReader(file)
    for i in reader:
        if i['code'] == waluta:
            sprzedaz = float(i['ask'])
            przelicznik = kwota * sprzedaz
            print(f'{przelicznik:.2f}')