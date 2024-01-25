from time import sleep

from bs4 import BeautifulSoup
from database import DatabaseHandler
from web_scraping import WebScraper

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

db_handler = DatabaseHandler()
web_scraper = WebScraper(headers)

with db_handler.connect() as db:
    c = db_handler.create_cursor(db)
    db_handler.create_table(c)
    db_handler.delete_all_rows(c)

    for p in range(1, 3):
        print(p)
        sleep(3)
        url = f"https://www.immowelt.de/suche/landkreis-steinburg/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp={p}"
        page_content = web_scraper.parse_page(url)

        if page_content is None:
            continue

        soup = BeautifulSoup(page_content, 'lxml')
        onepageFlats = soup.findAll('div', class_='EstateItem-4409d')

        data = [web_scraper.extract_flat_data(flat) for flat in onepageFlats]

        # Добавление данных
        db_handler.insert_data(c, data)

    # Закрываем соединение после каждой итерации
    db.commit()

print("Data successfully inserted into the database.")

