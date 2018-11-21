

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.otodom.pl/sprzedaz/mieszkanie/krakow/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w', encoding='utf-8', errors = 'ignore')  # zapis

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['nazwa', 'podpis', 'pokoj', 'metry', 'cena_metr', 'cena'])

for mieszkanie in soup.find_all(class_='offer-item-details'):

    nazwa = [mieszkanie.find('span', class_='offer-item-title').text]
    podpis = mieszkanie.find('p', class_='text-nowrap hidden-xs').text
    dzielnica = podpis.split(':')[1]
    pokoj = [mieszkanie.find('li', class_='offer-item-rooms hidden-xs').text]
    metry = [mieszkanie.find('li', class_='hidden-xs offer-item-area').text]
    cena_metr = [mieszkanie.find('li', class_='hidden-xs offer-item-price-per-m').text]
    cena = [mieszkanie.find('li', class_='offer-item-price').text]

    csv_writer.writerow([nazwa, dzielnica, pokoj, metry, cena_metr, cena])

csv_file.close()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", nazwa=[nazwa], dzielnica=[dzielnica], pokoj=[pokoj], metry=[metry], cena_metr=[cena_metr], cena=[cena])

if __name__ == "__main__":
    app.run()