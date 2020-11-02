from bs4 import BeautifulSoup
from requests import get
from utils.files import save_to_csv

serials_dict = {
}

def parse_page(url):
    serials = []
    ratings = []
    serials_wrapped, ratings_wrapped = find_information(url)
    for ser in serials_wrapped:
        serials.append(ser.text)
    for rate in ratings_wrapped:
        ratings.append(rate.text)
    return serials, ratings

def add_serials_to_dict(serials, ratings):
    for i in range(0, len(serials)):
        if ratings[i] != '—':
            serials_dict[serials[i]] = ratings[i]
    

def find_information(url):
    page = get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    serials = soup.findAll('p', class_='selection-film-item-meta__name')
    ratings = soup.findAll('span', class_='rating__value')
    return serials, ratings

def run_app():
    for i in range(1, 10):
        serials, ratings = parse_page(f'https://www.kinopoisk.ru/popular/films/?page={i}&sort=popularity&quick_filters=serials&tab=all')
        add_serials_to_dict(serials, ratings)
        save_to_csv(serials_dict)