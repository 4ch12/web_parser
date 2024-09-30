import datetime
import json
import re
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
            linkFlat = flat.find('a', class_="css-xt08q3").get('href')
            linkFlat = "https://www.immowelt.de"+linkFlat
            print("linkFlatWEBSCRBER:",linkFlat)

        except:
            linkFlat = 'linkFlat_not_found'
        try:
            # Найдем нужный div с атрибутом data-testid="classified-card-mfe-24XZZSY4A58R"
            # classified_card = flat.find('div', attrs={'data-testid': 'classified-card-mfe-24XZZSY4A58R'})

            # Извлекаем ссылку <a> внутри этого div
            # titleFlat = flat.find('a', attrs={'data-testid': 'card-mfe-covering-link-testid'}).get_text(strip=True)
            titleFlat = flat.find('a', class_="css-xt08q3").get('title')


            # Получаем значение атрибута title
            # titleFlat = titleFlat['title']
            print("titleFlatWEBSCRBER:", titleFlat)
        except:
            titleFlat = 'titleFlat_not_found'
        try:
            # Получаем адрес квартиры
            locationFlat = flat.find('div', class_='css-ymsudv', attrs={'data-testid': 'cardmfe-description-box-address'}).get_text(strip=True)
            print("locationFlatWEBSCRBER:", locationFlat)
        except:
            locationFlat = 'locationFlat_not_found'
            print("locationFlatWEBSCRBER::", locationFlat)
        try:
            wrongPriceFlat = flat.find('div', class_='KeyFacts-073db').find('div').get_text(strip=True)
        except:
            wrongPriceFlat = 'wrongPriceFlat_not_found'
    
    
        #Время парсинга 
        timeUpdate = datetime.datetime.now()
        timeUpdate = timeUpdate.strftime('%Y-%m-%d %H:%M:%S')

    #     return {
    #     'linkFlat': linkFlat,
    #     'titleFlat': titleFlat,
    #     'locationFlat': locationFlat,
    #     'wrongPriceFlat': wrongPriceFlat
    # }
        # Проверяем наличие NULL перед добавлением в базу данных
        # return linkFlat, titleFlat, locationFlat, wrongPriceFlat, timeUpdate
        return linkFlat, titleFlat, locationFlat, wrongPriceFlat, timeUpdate


    # def preise_flat_info(self, prise_flat):
    #     sleep(2)
    #     # Проверяем наличие элементов перед извлечением текста
    #     try:
    #         Kaltmiete = prise_flat.find('strong', class_="ng-star-inserted").get_text(strip=True)
    #     except:
    #         Kaltmiete = 'Kaltmiete_not_found'

    #     return Kaltmiete
