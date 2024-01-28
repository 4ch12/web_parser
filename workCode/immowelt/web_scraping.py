import datetime
import json
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
        # Проверяем наличие элементов перед извлечением текста
        try:
            linkFlat = flat.find('a', class_="mainSection-88b51 noProject-889ca").get('href')
        except:
            linkFlat = 'linkFlat_not_found'
        try:
            titleFlat = flat.find('h2').get_text(strip=True)
        except:
            titleFlat = 'titleFlat_not_found'
        try:
            locationFlat = flat.find('div', class_='IconFact-c55e4').find('span').get_text(strip=True)
        except:
            locationFlat = 'locationFlat_not_found'
        try:
            wrongPriceFlat = flat.find('div', class_='KeyFacts-073db').find('div').get_text(strip=True)
        except:
            wrongPriceFlat = 'wrongPriceFlat_not_found'
    
    
        #Время парсинга 
        timeUpdate = datetime.datetime.now()

    #     return {
    #     'linkFlat': linkFlat,
    #     'titleFlat': titleFlat,
    #     'locationFlat': locationFlat,
    #     'wrongPriceFlat': wrongPriceFlat
    # }
        # Проверяем наличие NULL перед добавлением в базу данных
        return linkFlat, titleFlat, locationFlat, wrongPriceFlat, timeUpdate

    