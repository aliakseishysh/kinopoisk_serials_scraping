from bs4 import BeautifulSoup
import requests
from utils.files import save_to_csv

serials_dict = {
}

def get_page(url):
    return requests.get(url)

def parse_page(url):
    serials_wrapped = []
    serials = []
    ratings_wrapped = []
    ratings = []
    serials_wrapped = find_serials(url)
    for ser in serials_wrapped:
        serials.append(ser.text)
    ratings_wrapped = find_ratings(url)
    for rate in ratings_wrapped:
        ratings.append(rate.text)
    return serials, ratings

def add_serials_to_dict(serials, ratings):
    for i in range(0, len(serials)):
        if ratings[i] != '—':
            serials_dict[serials[i]] = ratings[i]
    

def find_serials(url):
    soup = BeautifulSoup(get_page(url).text, 'html.parser')
    return soup.findAll('p', class_='selection-film-item-meta__name')

def find_ratings(url):
    soup = BeautifulSoup(get_page(url).text, 'html.parser')
    return soup.findAll('span', class_='rating__value')

def main():
    for i in range(1, 10):
        serials, ratings = parse_page(f'https://www.kinopoisk.ru/popular/films/?page={i}&sort=popularity&quick_filters=serials&tab=all')
        add_serials_to_dict(serials, ratings)
        save_to_csv(serials_dict)

main()