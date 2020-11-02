from bs4 import BeautifulSoup
from requests import get
from utils.files import write_headers, save_to_csv

 
def parse_page(url):
    page = get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    serials = soup.find_all('p', class_='selection-film-item-meta__name')
    ratings = soup.find_all('span', class_='rating__value')
    return dict(zip(
        [serial.text for serial in serials],
        [rating.text for rating in ratings]
        ))
  

def get_kwargs(**kwargs):
    return  kwargs.get('file_path'), \
            kwargs.get('page'), \
            kwargs.get('last_page'), \
            kwargs.get('sort'), \
            kwargs.get('quick_filters')

def make_filter_string(sort, quick_filters):
    filters = ''
    filters = filters + f'&sort={sort}' if sort else filters
    filters = filters + f'&quick_filters={quick_filters}' if quick_filters else filters
    filters = filters + '&tab=all'
    return filters
            
def run_app(**kwargs):

    url = "https://www.kinopoisk.ru/popular/films/?"
    
    # Get All Kwargs
    file_path, page, last_page, sort, quick_filters = get_kwargs(**kwargs)

    # Make Filter String
    filters = make_filter_string(sort, quick_filters)
    
    # Start Scraping
    if page:
        page = int(page)
        last_page = int(last_page) + 1 if last_page else page + 1

        write_headers(file_path, 'Название', 'Рейтинг')
        for current_page in range(page, last_page):
            save_to_csv(
                file_path, 
                parse_page(f'{url}page={current_page}{filters}')
            ) 