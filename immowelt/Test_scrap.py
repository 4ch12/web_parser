# import json
# import re
# from bs4 import BeautifulSoup
# import requests
# import time

# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/sMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "cookie": "bx=7d6510b5a2614fb5bf77445ac66af3ba; wd=ff918b79fd9e4553915f73b079494754; _gcl_au=1.1.1967548931.1727616765; _hjSessionUser_1377412=eyJpZCI6IjRlZTZiOWRhLWQ5ZTctNTA0NS1hNTIzLTY2MmIzNmI4M2QwZSIsImNyZWF0ZWQiOjE3MjM1NDM0NDY5OTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; kameleoonVisitorCode=d2t8q790plowwmus; datadome=AMAagC5RCh77zC~LbHqjFiA30Heyt4TvTjyUehpSPi9CMd15AR1UvW6v74uPR~wTzEOcb4aS1wCIMvgPntRcbdYea4LQboSDE~o1CFNqQ3cKz_O3CbjA0tPrZtemzMp9; utag_main=v_id:01923dfbc73100129f2fb068737d05075006306d00fb8$_sn:3$_se:8$_ss:0$_st:1727622746047$ses_id:1727620938807%3Bexp-session$_pn:3%3Bexp-session; IwAGSessionId=016f5914-7f95-d53e-3c02-b35240aeb900; _dd_s=logs=0&expire=1727621853654&rum=2&id=6859f91a-fe70-4bce-912e-49c515c6f13e&created=1727620941401"
# }

# regionStorage = ["landkreis-steinburg"]
# sizeRegionStorage = len(regionStorage)

# def web_scraper1(flat1):
#     """Функция для извлечения информации о квартире."""
#     try:
#         locationFlat = flat1.find('div', attrs={'data-testid': 'cardmfe-description-box-address'})
        
#         print("locationFlatWEBSCRBER::", locationFlat)
#         return locationFlat
#     except Exception as e:
#         locationFlat = 'locationFlat_not_found'
#         print("locationFlatWEBSCRBER::", locationFlat, "Ошибка:", e)
#         return locationFlat

# for po in range(sizeRegionStorage):
#     url = f"https://www.immowelt.de/suche/{regionStorage[po]}/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp=1"
#     print(f"URL: {url}")

#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'lxml')

#         # Найти все квартиры на странице
#         onepageFlats = soup.findAll('div', attrs={'data-testid': 'serp-card-testid'})
#         print(f"Найдено квартир: {len(onepageFlats)}")
#         print(onepageFlats)

#         data1 = [web_scraper1(flat1) for flat1 in onepageFlats]
#         for element in data1:
#             print('Вывод каждой квартиры с информацией после парсинга:', element)
#     else:
#         print(f"Ошибка запроса, статус-код: {response.status_code}")

#     # Задержка для снижения нагрузки на сервер
#     time.sleep(1)  # 1 секунда задержки

# import json
# import re
# from bs4 import BeautifulSoup
# import requests
# import time

# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/sMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "cookie": "bx=7d6510b5a2614fb5bf77445ac66af3ba; wd=ff918b79fd9e4553915f73b079494754; _gcl_au=1.1.1967548931.1727616765; _hjSessionUser_1377412=eyJpZCI6IjRlZTZiOWRhLWQ5ZTctNTA0NS1hNTIzLTY2MmIzNmI4M2QwZSIsImNyZWF0ZWQiOjE3MjM1NDM0NDY5OTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; kameleoonVisitorCode=d2t8q790plowwmus; datadome=AMAagC5RCh77zC~LbHqjFiA30Heyt4TvTjyUehpSPi9CMd15AR1UvW6v74uPR~wTzEOcb4aS1wCIMvgPntRcbdYea4LQboSDE~o1CFNqQ3cKz_O3CbjA0tPrZtemzMp9; utag_main=v_id:01923dfbc73100129f2fb068737d05075006306d00fb8$_sn:3$_se:8$_ss:0$_st:1727622746047$ses_id:1727620938807%3Bexp-session$_pn:3%3Bexp-session; IwAGSessionId=016f5914-7f95-d53e-3c02-b35240aeb900; _dd_s=logs=0&expire=1727621853654&rum=2&id=6859f91a-fe70-4bce-912e-49c515c6f13e&created=1727620941401"
# }

# regionStorage = ["landkreis-steinburg"]
# sizeRegionStorage = len(regionStorage)

# def web_scraper1(flat1):
#     """Функция для извлечения информации о квартире и названии города."""
#     try:
#         # Получаем адрес квартиры
#         address_div = flat1.find('div', class_='css-ymsudv', attrs={'data-testid': 'cardmfe-description-box-address'})
#         address = address_div.get_text(strip=True) if address_div else None
        
#         if address:
#             # Извлекаем название города с помощью регулярных выражений
#             city_match = re.search(r'([^,()]+)(?:\s*\(\d{5}\))?$', address)
#             city = city_match.group(1).strip() if city_match else 'City not found'
#         else:
#             city = 'City not found'
        
#         print("locationFlatWEBSCRBER::", address)
#         print("Город:", city)
        
#         return city  # Возвращаем только название города
#     except Exception as e:
#         print("Ошибка при извлечении информации:", e)
#         return 'City not found'

# for po in range(sizeRegionStorage):
#     url = f"https://www.immowelt.de/suche/{regionStorage[po]}/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp=1"
#     print(f"URL: {url}")

#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'lxml')

#         # Найти все квартиры на странице
#         onepageFlats = soup.findAll('div', attrs={'data-testid': 'serp-card-testid'})
#         print(f"Найдено квартир: {len(onepageFlats)}")

#         data1 = [web_scraper1(flat1) for flat1 in onepageFlats]
#         for city in data1:
#             print('Город после парсинга:', city)
#     else:
#         print(f"Ошибка запроса, статус-код: {response.status_code}")

#     # Задержка для снижения нагрузки на сервер
#     time.sleep(1)  # 1 секунда задержки


# import requests
# from bs4 import BeautifulSoup
# import re

# url = "https://www.immowelt.de/suche/landkreis-steinburg/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp=1"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# # Найдем все адреса квартир
# addresses = soup.find_all(string=re.compile("locationFlatWEBSCRBER::"))
# cities = []

# for address in addresses:
#     # Извлечем город из строки
#     match = re.search(r'\((\d{5})\)', address)
#     if match:
#         city_info = address.split(",")[-1].strip()
#         city_name = city_info.split("(")[0].strip() if city_info else "City not found"
#         cities.append(city_name)
#     else:
#         city_name = address.split(",")[-1].strip() if address else "City not found"
#         cities.append(city_name if city_name else "City not found")

# # Удаляем дубликаты, если необходимо
# unique_cities = list(set(cities))

# # Выводим результаты
# for city in unique_cities:
#     print(f"Город после парсинга: {city}")


import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote


# Заголовки для запроса
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/sMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "cookie": "bx=7d6510b5a2614fb5bf77445ac66af3ba; wd=ff918b79fd9e4553915f73b079494754; _gcl_au=1.1.1967548931.1727616765; _hjSessionUser_1377412=eyJpZCI6IjRlZTZiOWRhLWQ5ZTctNTA0NS1hNTIzLTY2MmIzNmI4M2QwZSIsImNyZWF0ZWQiOjE3MjM1NDM0NDY5OTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; kameleoonVisitorCode=d2t8q790plowwmus; datadome=AMAagC5RCh77zC~LbHqjFiA30Heyt4TvTjyUehpSPi9CMd15AR1UvW6v74uPR~wTzEOcb4aS1wCIMvgPntRcbdYea4LQboSDE~o1CFNqQ3cKz_O3CbjA0tPrZtemzMp9; utag_main=v_id:01923dfbc73100129f2fb068737d05075006306d00fb8$_sn:3$_se:8$_ss:0$_st:1727622746047$ses_id:1727620938807%3Bexp-session$_pn:3%3Bexp-session; IwAGSessionId=016f5914-7f95-d53e-3c02-b35240aeb900; _dd_s=logs=0&expire=1727621853654&rum=2&id=6859f91a-fe70-4bce-912e-49c515c6f13e&created=1727620941401"

}

# Список регионов
regionStorage = ["landkreis-steinburg"]
sizeRegionStorage = len(regionStorage)

def web_scraper1(flat1):
    """Функция для извлечения информации о квартире и названии города."""
    try:
        # Получаем адрес квартиры
        address_div = flat1.find('div', class_='css-ymsudv', attrs={'data-testid': 'cardmfe-description-box-address'})
        address = address_div.get_text(strip=True) if address_div else None
        print(f"Город address_div : {address_div}")
        if address:
            # Извлекаем название города с помощью регулярных выражений
            city_match = re.search(r'([^,()]+)(?:\s*\(\d{5}\))?$', address)
            city = city_match.group(1).strip() if city_match else f'City not found: {address}'
        else:
            city = 'City not found'
        
        print(f"Город после парсинга: {city}")
        
        return city  # Возвращаем только название города или ошибку с адресом
    except Exception as e:
        print("Ошибка при извлечении информации:", e)
        return 'City not found'

# Цикл по каждому региону
for po in range(sizeRegionStorage):
    # Кодируем URL
    region = quote(regionStorage[po])
    url = f"https://www.immowelt.de/suche/{region}/wohnungen/mieten?d=true&sd=DESC&sf=RELEVANCE&sp=1"
    print(f"URL: {url}")

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')

        # Найти все квартиры на странице
        onepageFlats = soup.findAll('div', attrs={'data-testid': 'serp-card-testid'})
        print(f"Найдено квартир: {len(onepageFlats)}")

        # Извлечение данных о квартирах
        data1 = [web_scraper1(flat1) for flat1 in onepageFlats]

    else:
        print(f"Ошибка запроса, статус-код: {response.status_code}")
