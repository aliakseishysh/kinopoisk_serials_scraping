if __name__ == '__main__':
    from sys import argv
    from scraper.scraper import run_app
    kwargs = dict(arg.split('=') for arg in argv[1:])
    run_app(**kwargs)
