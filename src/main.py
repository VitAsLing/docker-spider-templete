# main.py

from src.scraper.web_scraper import open_webpage_with_chrome

if __name__ == '__main__':
    page = open_webpage_with_chrome("https://google.com")
    print(page)
