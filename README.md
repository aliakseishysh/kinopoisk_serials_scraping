# Scrape serials/films from kinopoisk.ru
# TODO
    1) Make async requests

To run script:
    python run.py 
        file_path={your_file_name.csv} 
        [page={start page to scrape}]
        [sort={type of sorting}]
        [quick_filters={type of content}]
        [last_page={last page to scrape}]

    sort  = [
                'popularity',
                'votes',
                'year',
                'title',
            ]

    quick_filters = [
                        'films', 
                        'serials',
                    ]
