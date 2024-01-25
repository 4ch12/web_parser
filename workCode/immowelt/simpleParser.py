import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# Подключаемся к базе данных с использованием контекстного менеджера
with sqlite3.connect('allFlat.db') as db:
    # Создаем объект курсора
    c = db.cursor()

    # Удаляем все строки из таблицы перед добавлением новых данных
    c.execute("DELETE FROM allFlatsAfterParsoing")

    for p in range(1, 3):
        print(p)
        sleep(3)
        url = f"https://www.immowelt.de/suche/landkreis-steinburg/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp={p}"

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()  # Проверка наличия ошибок при запросе
        except requests.exceptions.RequestException as err:
            print("Error:", err)
            continue  # Пропустить текущую итерацию цикла, если произошла ошибка

        soup = BeautifulSoup(response.text, 'lxml')
        onepageFlats = soup.findAll('div', class_='EstateItem-4409d')

        for flat in onepageFlats:
            linkFlat = flat.find('a', class_="mainSection-88b51 noProject-889ca")
            titleFlat = flat.find('h2')
            locationFlat = flat.find('div', class_='IconFact-c55e4').find('span')
            wrongPriceFlat = flat.find('div', class_='KeyFacts-073db').find('div')

            # Проверяем наличие элементов перед извлечением текста
            linkFlat = linkFlat.get('href') if linkFlat else 'notFound for linkFlat'
            titleFlat = titleFlat.get_text(strip=True) if titleFlat else 'notFound for titleFlat'
            locationFlat = locationFlat.get_text(strip=True) if locationFlat else 'notFound for locationFlat'
            wrongPriceFlat = wrongPriceFlat.get_text(strip=True) if wrongPriceFlat else 'notFound for wrongPriceFlat'

            # Проверяем наличие NULL перед добавлением в базу данных
            if None in (linkFlat, titleFlat, locationFlat, wrongPriceFlat):
                continue

            # Добавление данных
            c.execute("""
                INSERT INTO allFlatsAfterParsoing (linkFlat, titleFlat, locationFlat, truePriceFlat)
                VALUES (?, ?, ?, ?)
            """, (linkFlat, titleFlat, locationFlat, wrongPriceFlat))

        # Закрываем соединение после каждой итерации
        db.commit()

# Вывод данных после завершения цикла
print("Data successfully inserted into the database.")




# print(len(data))
# print(data)

       

 


    
    # data = []
    # onepageFlats = soup.findAll('div', class_='EstateItem-4409d')
    # for flat in onepageFlats:
    #   linkFlat = soup.find('a', class_="mainSection-88b51 noProject-889ca").get('href')
    #   titleFlat = soup.find('h2').get_text(strip=True)
    #   locationFlat = soup.find('div', class_='IconFact-c55e4').find('span').get_text(strip=True)
    #   wrongPriceFlat = soup.find('div', class_='KeyFacts-073db').find('div').get_text(strip=True)
      
    # data.append([linkFlat, titleFlat, locationFlat, wrongPriceFlat])
    # match = re.search(r'\d+', wrongPriceFlat)
    # truePriceFlat = str(match.group())
    # separator = '\n'
    # result = separator.join(data[(int(len(onepageFlats))-1)])
    # print(data)
    # print(result) 
    
    

    
    #print(match) 

    # flat1 = [linkFlat, titleFlat, locationFlat, truePriceFlat]
    # separator = '\n'
    # result = separator.join(flat1)
    # print(result) 


   # print(soup.find('div', class_='FactsMain-24dde').find('div', class_='KeyFacts-073db').find('div').get_text(strip=True))   # головна інфо price,area,rooms,location
   # with open("index.html", "w") as file:
    #   file.write(response.text)   
   
 


 # Преобразуем данные в строку для вывода
        #result = '\n'.join([','.join(map(str, flat)) for flat in data])
    # for i in range(legnthItems):
    #   result = data[і]
    #   legnthItems = int(len(onepageFlats))
    #   print(legnthItems)
    #   print(result)