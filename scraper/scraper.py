from bs4 import BeautifulSoup
from requests import get
from utils.files import write_headers, save_to_csv
from concurrent.futures import ThreadPoolExecutor

 
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
    return \
            kwargs.get('file_name'), \
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


def build_urls(page, last_page, filters):
    base_url = "https://www.kinopoisk.ru/popular/films/?"
    urls = []
    if page:
        page = int(page)
        last_page = int(last_page) + 1 if last_page else page + 1

        for current_page in range(page, last_page):
            urls.append(f'{base_url}page={current_page}{filters}')

        return urls


def run_app(**kwargs):

    # Get All Kwargs
    file_name, page, last_page, sort, quick_filters = get_kwargs(**kwargs)

    # Make Filter String
    filters = make_filter_string(sort, quick_filters)

    # Make urls
    urls = build_urls(page, last_page, filters)

    # Start Scraping
    write_headers(file_name, 'Название', 'Рейтинг')

    with ThreadPoolExecutor(3) as executor:
        results = executor.map(parse_page, urls)

    for result in results:
        save_to_csv(
            file_name,
            result
        )
