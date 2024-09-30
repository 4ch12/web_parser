import time
import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3
import tqdm
from config import MyFlat
import re


headers = {
    
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/sMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "cookie":"bx=7d6510b5a2614fb5bf77445ac66af3ba; wd=ff918b79fd9e4553915f73b079494754; _gcl_au=1.1.1967548931.1727616765; _hjSessionUser_1377412=eyJpZCI6IjRlZTZiOWRhLWQ5ZTctNTA0NS1hNTIzLTY2MmIzNmI4M2QwZSIsImNyZWF0ZWQiOjE3MjM1NDM0NDY5OTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; kameleoonVisitorCode=d2t8q790plowwmus; datadome=AMAagC5RCh77zC~LbHqjFiA30Heyt4TvTjyUehpSPi9CMd15AR1UvW6v74uPR~wTzEOcb4aS1wCIMvgPntRcbdYea4LQboSDE~o1CFNqQ3cKz_O3CbjA0tPrZtemzMp9; utag_main=v_id:01923dfbc73100129f2fb068737d05075006306d00fb8$_sn:3$_se:8$_ss:0$_st:1727622746047$ses_id:1727620938807%3Bexp-session$_pn:3%3Bexp-session; IwAGSessionId=016f5914-7f95-d53e-3c02-b35240aeb900; _dd_s=logs=0&expire=1727621853654&rum=2&id=6859f91a-fe70-4bce-912e-49c515c6f13e&created=1727620941401"
}



def inner_parser():
    kaltmiete_value, nebenkosten_value, heizkosten_value, warmmiete_value, stellplatz_value,qm_value = [None] * 6
    heizkosten_in_Warmmiete_enthalten, heizkosten_nicht_in_Warmmiete_enthalten,kaltmiete_zzgl_value= [None] * 3

    try:
            sqlite_connection = sqlite3.connect('allFlat.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            
            sqlite_select_query = "SELECT * from allFlatsAfterParsoing1"
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Строки: ",records)
            print("Всего строк: ", len(records))
            print("Вывод каждой строки")
                    # for row in  tqdm.tqdm(records):
                    # time.sleep(0.1)
            for row in  tqdm.tqdm(records):
                    time.sleep(0.1)
                    links_flat = row[1]
                    print(links_flat)
                    location_flat =  row[3]
                    print(location_flat)
                    sleep(2)
                    print("LINKS:", links_flat),
                    print("Location:", location_flat, end="\n")
                    # Переменные для хранения значений
                    print(links_flat,"JUST CYCLE")
                    print('___________'*20)
                    
                    url = f"{links_flat}"
                    print(links_flat)
                    if url == "linkFlat_not_found":
                        print("linkFlat_not_found + ХУЙНЯ")    
                    else:
                        response = requests.get(url=url, headers=headers)
                    
                    soup = BeautifulSoup(response.text, 'lxml')
                    print('response.text'*20)
                    print(response.text)
                    # получаю квадратуру квартиры 
                    #  # Ищем элемент <span> с классом 'css-2bd70b' и получаем его текст
                    #     qm = soup.find('h1', class_='css-qk4947').get_text()
                    #     print('qmsoup',qm )
                    # qmsoup Wohnung zur Miete305 €305 €Kaltmiete zzgl. NebenkostenSCHUFA-BonitätscheckGesponsert2Zimmer29 m²Wohnfläche1.Geschoss01.10.2024VerfügbarkeitKlaus-Groth-Straße 7, Glückstadt (25348)
                
                

                    try:
                        # Ищем все элементы с классом 'css-jtsp8r'
                        qm_elements = soup.findAll('div', class_='css-jtsp8r')
                        
                        # Проходим по всем найденным элементам
                        for element in qm_elements:
                            # Получаем текст каждого элемента
                            qm = element.get_text()
                            print('qmsoup:', qm)
                            
                            # Используем регулярное выражение для поиска числа перед "m²"
                            match = re.search(r'(\d+)\s?m²', qm)
                            if match:
                                qm_value = match.group(1)  # Извлекаем первое число перед "m²"
                                print("qm_value:", qm_value)
                                break  # Прерываем цикл, если нашли значение площади
                        else:
                            # Если элемент с "m²" не найден
                            qm_value = 'qm_not_found'
                    except AttributeError:  # Если элемент не найден
                        qm_value = 'qm_not_found'
                        print("Error: 'css-jtsp8r' div not found")
                    except Exception as e:  # Обработка других ошибок
                        qm_value = 'qm_not_found'
                        print(f"Unexpected error: {e}")




                    # price_block = soup.find_all('span', class_='css-9wpf20')
                    price_block = soup.find_all('div', class_='css-q6n4wc')
                
                    print('price_block',price_block)
                    prices_flat_data = []
                    print('prices_flat_data',prices_flat_data)

                    for tag in price_block:
                        try:
                            prise_flat = tag.get_text().replace('€', ' ').strip()
                            print('prise_flat',prise_flat)

                        except:
                            prise_flat = 'Prise_flat_not_found'
                            print('Prise_flat_not_found',prise_flat)

                        prices_flat_data.append(prise_flat)
                        print('prices_flat_data',prices_flat_data)

                # Инициализация переменных перед циклом
                    kaltmiete_value = None
                    nebenkosten_value = None
                    heizkosten_value = None
                    heizkosten_in_Warmmiete_enthalten = None
                    heizkosten_nicht_in_Warmmiete_enthalten = None
                    warmmiete_value = None
                    stellplatz_value = None

                    for item in prices_flat_data:
                        # Разделение строки по пробелу и получение последнего элемента
                        value = item.split()[-1].strip()
                        print('___________Разделение строки по пробелу__________________')
                        print(value)

                        # Проверка, к какой категории относится текущая строка и присвоение значения соответствующей переменной
                        if 'Kaltmiete zzgl.' in item:
                            kaltmiete_zzgl_value = True
                        elif 'Kaltmiete' in item:
                            kaltmiete_value = value
                        elif 'Heizkosten' in item:
                            try:
                                heizkosten_value = ''.join(filter(str.isdigit, value))
                            except ValueError:
                                heizkosten_value = 0
                        elif 'Nebenkosten' in item:
                            nebenkosten_value = value
                        elif 'Heizkostenin Warmmiete enthalten' in item:
                            heizkosten_in_Warmmiete_enthalten = True
                        elif 'nicht in Warmmiete enthalten' in item:
                            heizkosten_nicht_in_Warmmiete_enthalten = True
                        elif 'Warmmiete' in item:
                            warmmiete_value = value
                        elif 'Stellplatz' in item:
                            stellplatz_value = value


                    # Вывод значений переменных
                    print('___________Вывод значений переменных__________________')
                    print(f"Kaltmiete: {kaltmiete_value}")
                    print(f"Nebenkosten:  {nebenkosten_value}")
                    print(f"Heizkosten: {heizkosten_value}")
                    print(f"Heizkosten in Warmmiete enthalten: {heizkosten_in_Warmmiete_enthalten}")
                    print(f"Heizkosten_nicht_in_Warmmiete_enthalten: {heizkosten_nicht_in_Warmmiete_enthalten}")
                    print(f"Warmmiete: {warmmiete_value}")
                    print(f"Stellplatz: {stellplatz_value}")
                    print(f"m² : {qm_value}")


                    print("______Убрать точки в числах,в kaltmiete nebenkosten_________")
                    # Преобразование строки в число с плавающей точкой
                    # try:
                    #     if '.' not in kaltmiete_value and ',' not in kaltmiete_value:
                    #         kaltmiete = float(kaltmiete_value)
                    #         # print(kaltmiete,'kaltmiete_not')
                    #     elif '.'and',' in kaltmiete_value:
                    #         kaltmiete = kaltmiete_value.split(',')[0].replace('.' , '')+ '.' + kaltmiete_value.rsplit(',', 1)[1]
                    #         kaltmiete = float(kaltmiete)
                    #         # print(kaltmiete,'kaltmiete_dot_coma')
                    #     elif ',' in kaltmiete_value:
                    #         kaltmiete = kaltmiete_value.replace(',' , '.')
                    #         kaltmiete = ''.join(kaltmiete) 
                    #         kaltmiete = float(kaltmiete)
                    #         # print(kaltmiete,'kaltmiete_coma')
                    #     elif '.' in kaltmiete_value:
                    #         kaltmiete= kaltmiete_value.replace('.' , '')
                    #         kaltmiete = float(kaltmiete)
                    #         # print(kaltmiete,'kaltmiete_dot')
                        
                    #         # print("Строка не содержит ни '.' ни ','")        
                    # except ValueError:
                    #     # Обработка случая, когда строка не может быть преобразована в число
                    #     kaltmiete = 0.0
                    
                    # Преобразование строки в число с плавающей точкой
                    try:
                        # Check if kaltmiete_value is None or not a string
                        if kaltmiete_value is None or not isinstance(kaltmiete_value, str):
                            kaltmiete = 0.0  # Set a default value if kaltmiete_value is None
                        else:
                            if '.' not in kaltmiete_value and ',' not in kaltmiete_value:
                                kaltmiete = float(kaltmiete_value)
                                print(kaltmiete,'kaltmiete_not')
                            elif '.' in kaltmiete_value and ',' in kaltmiete_value:
                                kaltmiete = kaltmiete_value.split(',')[0].replace('.', '') + '.' + kaltmiete_value.rsplit(',', 1)[1]
                                kaltmiete = float(kaltmiete)
                                print(kaltmiete,'kaltmiete_dot_coma')
                            elif ',' in kaltmiete_value:
                                kaltmiete = kaltmiete_value.replace(',', '.')
                                kaltmiete = float(kaltmiete)  # Convert to float
                                print(kaltmiete,'kaltmiete_coma')
                            elif '.' in kaltmiete_value:
                                kaltmiete = kaltmiete_value.replace('.', '')
                                kaltmiete = float(kaltmiete)  # Convert to float
                                print(kaltmiete,'kaltmiete_dot')
                    except ValueError:
                        # Обработка случая, когда строка не может быть преобразована в число
                        kaltmiete = 0.0


                    if nebenkosten_value is not None:
                        nebenkosten = nebenkosten_value.replace(',', '.')
                        nebenkosten = ''.join(nebenkosten) 
                        nebenkosten = float(nebenkosten)
                        nebenkosten = round(nebenkosten, 1)
                        print(nebenkosten,"nebenkosten")
                    else:
                        nebenkosten = 0.0
                    

                    qm = qm_value.replace(',', '.') if qm_value else 0
                    print(f"kaltmiete: {kaltmiete}, nebenkosten: {nebenkosten}")


                    print("______Сложение (kaltmiete+nebenkosten) _________")
                    gesammite = kaltmiete + nebenkosten
                    print('Gesammite : ', gesammite)

                    print("______Сравнение по городам и их лимитам (locationFlat и gesammite), еще нужна квадратура до 50 квм. _________")
                    param_flat = {
                    'Itzehoe': 454.25,
                    'GlÃ¼ckstadt': 445.09,
                    'Herzhorn': 445.09,
                    'Horst': 445.09,
                    'Krempe': 411.68,
                    'Kremperheide': 411.68,
                    'Wilster': 411.68,
                    'Elmshorn': 510.2,
                    'Pinneberg': 559.2,
                    'Tornesh': 559.2,
                    'Kiel': 439}
                    print("Location:", location_flat)
                    
                    for city,value in param_flat.items():
                        if city in location_flat and gesammite <= value:
                        # and gesammite <= value:
                            print("Город найден в списке:", city)
                            print("Соответствующее значение:", value,end="\n\n")
                            my_flat = MyFlat()
                            my_flat.test(city,gesammite, links_flat, nebenkosten, heizkosten_value)
                            my_flat.print_values()

                            break
                        else:
                            a=0
                        print("Город не найден в списке.")
                    
                    print("Цикл закончился",end="\n\n")
                        
    
    except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
    
    # finally:
    #     if sqlite_connection:
                
    #             sqlite_connection.close()
    #             print("Соединение с SQLite закрыто")
    cursor.close()
    print("Data successfully inserted into the database.")
    
