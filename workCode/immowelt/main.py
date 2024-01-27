import datetime
from time import sleep
import json
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

    # db_handler.create_table(c)
    # print("create_table") 
    # db_handler.add_time_update_column(c)
    # print("add_time_update_column") 
    # db_handler.delete_all_rows(c)
    regionStorage = ["hamburg","landkreis-steinburg","landkreis-pinneberg","kiel","flensburg",
                    "neumuenster","luebeck-hansestadt","landkreis-stormarn","landkreis-segeberg",
                    "landkreis-schleswig-flensburg","landkreis-rendsburg-eckernfoerde","landkreis-ploen",
                    "landkreis-ostholstein","landkreis-nordfriesland","landkreis-herzogtum-lauenburg",
                    "landkreis-dithmarschen"]
    sizeRegionStorage = len(regionStorage)
    

    for po in range(0, sizeRegionStorage):
    # while True:
    # Здесь поместите код, который будет выполняться в каждой итерации цикла
       
        # int(offer_count/20)
        offer_count = 1
    for p in range(1, offer_count+1):
            print(p)
            sleep(3)
            url = f"https://www.immowelt.de/suche/{regionStorage[po]}/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp={p}"
            print(url)
            page_content = web_scraper.parse_page(url)
            soup = BeautifulSoup(page_content, 'lxml')
            scripts = soup.findAll('script')

            script_text = scripts[0].text.strip()
            print("# Получаем текст скрипта",script_text)
                        
            if 'offers' in script_text:
                json_str = script_text.split('>', 1)[0].split('</script>', 1)[0]
                print("# Находим JSON-структуру внутри скрипта",json_str)
                
                data1 = json.loads(json_str)
                print("Парсинг JSON-строки",data1)

                if 'offers' in data1 and 'offerCount' in data1['offers']:
                    offer_count = data1['offers']['offerCount']
                    print("Offer Count:", offer_count)
                
                # Получение значения "offerCount"
                    # data1 = json.loads(json_str)
                    # print("Парсинг JSON-строки")


                # # Проверяем, содержит ли скрипт JSON-структуру
                # if 'application/ld+json' in scripts[0]:

                #     # Найдите JSON-структуру внутри скрипта
                #     json_str = scripts[0].split('>', 1)[1].split('</script>', 1)[0]
                #     print(" # Найдите JSON-структуру внутри скрипта") 

                #     # Парсинг JSON-строки
                #     data1 = json.loads(json_str)
                #     print("Парсинг JSON-строки")

                #     # Получение значения "offerCount"
                #     if 'offers' in data1 and 'offerCount' in data1['offers']:
                #      offer_count = data1['offers']['offerCount']
                #      print("Offer Count:", offer_count)
           
            if page_content is None:
                continue
   
            
            # countPage = web_scraper.extra_page_info(soup)
            # countPage = soup.soup.find('div', class_="Pagination-190de").find('button', class_="Button-c3851 secondary-47144 navNumberButton-d264f").find('span').get_text(strip=True)
            # pagination_div = soup.findAll('div', class_="Pagination-190de")
            # print(pagination_div)
            # button = soup.find('div', class_='SearchResults-606eb').find('div', class_='Pagination-190de').find('div').find('button', class_='Button-c3851 secondary-47144 navNumberButton-d264f').find('span').get_text()
            
            # if script is None:
            #     continue
            # print(script)
            # if script != "long_arrow_right":
            #    break  # Выходим из цикла, если условие выполнено 
            
            # span = button.find('span')
            # print(span)
            # countPage = span.get_text(strip=True)
            # print(countPage)
            

            onepageFlats = soup.findAll('div', class_='EstateItem-4409d')
            data = [web_scraper.extract_flat_data(flat) for flat in onepageFlats]
        
            for element in data:
             print(element)
            
            

            # for value in data:
            #     link = value[0]  # Получаем ссылку из текущего элемента данных
            #     print(link)  
            #     index_to_compare = 'https://www.immowelt.de/expose/2dx7g59'
                
            #     if link == index_to_compare:
            #         print(f"Индекс {link} равен {index_to_compare}")
                    
            #     else:
            #         print("test  else")
            for row in data:
                linkFlat = row[0]
                titleFlat = row[1]
                locationFlat = row[2]
                truePriceFlat = row[3]
                timeUpdate = row[4]
            Newdata = [linkFlat,titleFlat,locationFlat,truePriceFlat, timeUpdate]
            
            # Обновление данных     
            db_handler.update_all_rows(c,Newdata) 
            # Добавление данных
            # db_handler.insert_data(c,Newdata)
        # Проверяем условие
     
    # Закрываем соединение после каждой итерации
    db.commit()
    # db.close()

print("Data successfully inserted into the database.")

# 
# 
# 
# 
# 
# 
# 
# 
# 