import json
import time
from bs4 import BeautifulSoup 
import requests
import tqdm 
from database import DatabaseHandler
from web_scraping import WebScraper
from simpleParser import inner_parser
import re

headers = {
    
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/sMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "cookie":"bx=7d6510b5a2614fb5bf77445ac66af3ba; wd=ff918b79fd9e4553915f73b079494754; _gcl_au=1.1.1967548931.1727616765; _hjSessionUser_1377412=eyJpZCI6IjRlZTZiOWRhLWQ5ZTctNTA0NS1hNTIzLTY2MmIzNmI4M2QwZSIsImNyZWF0ZWQiOjE3MjM1NDM0NDY5OTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; kameleoonVisitorCode=d2t8q790plowwmus; datadome=AMAagC5RCh77zC~LbHqjFiA30Heyt4TvTjyUehpSPi9CMd15AR1UvW6v74uPR~wTzEOcb4aS1wCIMvgPntRcbdYea4LQboSDE~o1CFNqQ3cKz_O3CbjA0tPrZtemzMp9; utag_main=v_id:01923dfbc73100129f2fb068737d05075006306d00fb8$_sn:3$_se:8$_ss:0$_st:1727622746047$ses_id:1727620938807%3Bexp-session$_pn:3%3Bexp-session; IwAGSessionId=016f5914-7f95-d53e-3c02-b35240aeb900; _dd_s=logs=0&expire=1727621853654&rum=2&id=6859f91a-fe70-4bce-912e-49c515c6f13e&created=1727620941401"
}

db_handler = DatabaseHandler()
web_scraper = WebScraper(headers)




with db_handler.connect() as db:
    c = db_handler.create_cursor(db)
        # Создание табл данных    
    db_handler.create_table(c)
    db.commit() 
    db_handler.delete_all_rows(c)
    db.commit() 

    regionStorage = ["landkreis-steinburg"]
    # regionStorage = ["AD06DE14","AD08DE1113"]
    # https://www.immowelt.de/classified-search?distributionTypes=Rent&estateTypes=Apartment&locations=AD06DE14
    # regionStorage = ["landkreis-steinburg","landkreis-pinneberg","kiel","flensburg",
    #                      "neumuenster","luebeck-hansestadt","landkreis-stormarn","landkreis-segeberg",
    #                      "landkreis-schleswig-flensburg","landkreis-rendsburg-eckernfoerde","landkreis-ploen",
    #                      "landkreis-ostholstein","landkreis-nordfriesland","landkreis-herzogtum-lauenburg",
    #                      "landkreis-dithmarschen"]
    sizeRegionStorage = len(regionStorage)

        
    for po in tqdm.tqdm(range(sizeRegionStorage)):
                # Ваш код здесь
                time.sleep(0.1)
                time.sleep(1)
                url = f"https://www.immowelt.de/suche/{regionStorage[po]}/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp=1"
                # url = f"https://www.immowelt.de/classified-search?distributionTypes=Rent&estateTypes=House,Apartment&locations={regionStorage[po]}"

                print(url)

                page_content = web_scraper.parse_page(url)
                soup = BeautifulSoup(page_content, 'lxml')
                scripts = soup.find_all("script")
                # scripts = soup.findAll('h1', attrs={'data-testid': 'serp-title-variant-a-testid'})
                script_text = scripts[0].text.strip()
                print("# Получаем текст скрипта",scripts,script_text)
                 # Найти все теги <script>
                print(f"Найдено {len(scripts)} скриптов на странице.")
                # Получаем текст скрипта
                
                    
                    # Проходим по всем найденным скриптам
                for idx, script in enumerate(scripts):
                        script_text = script.text.strip()

                        # Попробуем найти JSON-структуру
                        json_match = re.search(r'\{.*\}', script_text, re.DOTALL)
                        if json_match:
                            json_str = json_match.group(0)
                            print(f"Extracted JSON string from script {idx + 1}: {json_str[:1500]}...")

                            # Попытка парсинга JSON
                            try:
                                data1 = json.loads(json_str)
                                print("Успешный парсинг JSON-строки.")
                                
                                # Здесь можно работать с data1
                                if 'offers' in data1 and 'offerCount' in data1['offers']:
                                    offer_count = data1['offers']['offerCount']
                                    print("Offer Count:", offer_count)
                                    pageCount = int(offer_count / 20)
                                    print(f"Page Count: {pageCount}")

                            except json.JSONDecodeError as e:
                                print(f"Ошибка при разборе JSON: {e}")
                                print(f"Невалидная JSON-строка: {json_str[:500]}...")
                        else:
                            print(f"JSON не найден в скрипте {idx + 1}.")
                
                for p in range(1, pageCount+1): 
                    print(p)
                    time.sleep(1)
                    url = f"https://www.immowelt.de/suche/{regionStorage[po]}/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp={p}"
                            # url = f"https://www.immowelt.de/classified-search?distributionTypes=Rent&estateTypes=House&locations=AD08DE1113&page={p}"
                    print(url)
                    page_content = web_scraper.parse_page(url)
                    soup = BeautifulSoup(page_content, 'lxml')
                        
                    if page_content is None:    
                        continue

                    # onepageFlats = soup.findAll('div', class_='EstateItem-4409d')
                    onepageFlats = soup.findAll('div', attrs={'data-testid': 'serp-card-testid'})
                    print(onepageFlats)
                    # linkFlat = soup.find('a', class_="css-xt08q3").get('href')
                    # print("linkFlatMAIN:",linkFlat)
                    
                    
                 

                    data = [web_scraper.extract_flat_data(flat) for flat in onepageFlats]
                    print(data)
                    # Вывод каждой квартиры с информацией после парсинга 
                    for element in data:
                        print('Вывод каждой квартиры с информацией после парсинга ',element)
                    # if len(row) == 5:
                    #     linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate = row
                    # else:
                    #     print(f"Ошибка: ожидалось 5 значений, но получено {len(row)}: {row}")
                    
                    for row in data:
                        print('Вывод object data in main',data)
                        # linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate = row
                        linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate, *rest = row

                        Newdata = [linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate]

                    # Обновление данных   
                        # db_handler.update_all_rows(c,Newdata)
                        # db.commit()
                    # Добавление данных
                        db_handler.insert_data(c, Newdata)
                        db.commit()

                    
                        
        # Закрываем соединение после каждой итерации       
db.close()
print("Data successfully inserted into the database.")
inner_parser()

