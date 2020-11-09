# Scrape serials/films from kinopoisk.ru

To run script:

    python run.py 
        file_name={your_file_name.csv} 
        page={start page to scrape}
        [sort={type of sorting}]
        [quick_filters={type of content}]
        [last_page={last page to scrape}]

Filters:

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
