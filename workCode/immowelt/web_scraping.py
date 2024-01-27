import datetime
import requests
from bs4 import BeautifulSoup
from time import sleep

class WebScraper:
    def __init__(self, headers):
        self.headers = headers

    def parse_page(self, url):
        try:
            response = requests.get(url=url, headers=self.headers)
            response.raise_for_status()  # Проверка наличия ошибок при запросе
            return response.text
        except requests.exceptions.RequestException as err:
            print("Error:", err)
            return None
   
        

    def extract_flat_data(self, flat):
        sleep(2)
        linkFlat = flat.find('a', class_="mainSection-88b51 noProject-889ca")
        titleFlat = flat.find('h2')
        locationFlat = flat.find('div', class_='IconFact-c55e4').find('span')
        wrongPriceFlat = flat.find('div', class_='KeyFacts-073db').find('div')
        
        
        # Проверяем наличие элементов перед извлечением текста
        linkFlat = linkFlat.get('href') if linkFlat else 'notFound for linkFlat'
        titleFlat = titleFlat.get_text(strip=True) if titleFlat else 'notFound for titleFlat'
        locationFlat = locationFlat.get_text(strip=True) if locationFlat else 'notFound for locationFlat'
        wrongPriceFlat = wrongPriceFlat.get_text(strip=True) if wrongPriceFlat else 'notFound for wrongPriceFlat'
        #Время парсинга 
        timeUpdate = datetime.datetime.now()


        # Проверяем наличие NULL перед добавлением в базу данных
        return linkFlat, titleFlat, locationFlat, wrongPriceFlat, timeUpdate

    # def extra_page_info (self,soup):
        
        