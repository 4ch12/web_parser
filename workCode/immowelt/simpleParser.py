import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3
from config import MyFlat

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


kaltmiete_value, nebenkosten_value, heizkosten_value, warmmiete_value, stellplatz_value,qm_value = [None] * 6
heizkosten_in_Warmmiete_enthalten, heizkosten_nicht_in_Warmmiete_enthalten,kaltmiete_zzgl_value= [None] * 3

try:
    sqlite_connection = sqlite3.connect('allFlat.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    sqlite_select_query = """SELECT * from allFlatsAfterParsoing1"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    print("Вывод каждой строки")
            # for row in  tqdm.tqdm(records):
            # time.sleep(0.1)
    for row in  records:
            links_flat = row[0]
            location_flat =  row[2]
            sleep(2)
            print("LINKS:", links_flat),
            print("Location:", location_flat, end="\n")
            # Переменные для хранения значений
            # print(links_flat,"JUST CYCLE")
            # print('_____________________________')
            
            url = f"{links_flat}"
            print(links_flat)

            response = requests.get(url=url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            # получаю квадратуру квартиры 
            try:
                qm = soup.find('span',class_ = 'has-font-300').get_text()
                qm_value = qm.split()[0] 
            except:
                qm_value = 'qm_not_found'

            price_block = soup.find_all('sd-cell-row', class_='cell-size-100 cell__row ng-star-inserted')
    
            prices_flat_data = []
    

            for tag in price_block:
                try:
                    prise_flat = tag.get_text().replace('€', ' ').strip()
                    
                except:
                    prise_flat = 'Prise_flat_not_found'

                prices_flat_data.append(prise_flat)
            print(prices_flat_data)

            for item in prices_flat_data:
            # Разделение строки по пробелу и получение последнего элемента
                value = item.split()[-1] 
                # print('___________Разделение строки по пробелу__________________')
                # print(value)
                
                
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
                elif 'Heizkosten in Warmmiete enthalten' in item:
                    heizkosten_in_Warmmiete_enthalten = True
                elif 'Heizkosten nicht in Warmmiete enthalten' in item:
                    heizkosten_nicht_in_Warmmiete_enthalten = True
                elif 'Warmmiete' in item:
                    warmmiete_value = value
                elif 'Stellplatz' in item:
                    stellplatz_value = value

            # Вывод значений переменных
            # print('___________Вывод значений переменных__________________')
            print(f"Kaltmiete: {kaltmiete_value}")
            # print(f"Nebenkosten:  {nebenkosten_value}")
            # print(f"Heizkosten: {heizkosten_value}")
            # print(f"Heizkosten in Warmmiete enthalten: {heizkosten_in_Warmmiete_enthalten}")
            # print(f"Heizkosten_nicht_in_Warmmiete_enthalten: {heizkosten_nicht_in_Warmmiete_enthalten}")
            # print(f"Warmmiete: {warmmiete_value}")
            # print(f"Stellplatz: {stellplatz_value}")
            # print(f"m² : {qm_value}")  

            # print("______Убрать точки в числах,в kaltmiete nebenkosten_________")
            # Преобразование строки в число с плавающей точкой
            try:
                if '.' not in kaltmiete_value and ',' not in kaltmiete_value:
                    kaltmiete = float(kaltmiete_value)
                    # print(kaltmiete,'kaltmiete_not')
                elif '.'and',' in kaltmiete_value:
                    kaltmiete = kaltmiete_value.split(',')[0].replace('.' , '')+ '.' + kaltmiete_value.rsplit(',', 1)[1]
                    kaltmiete = float(kaltmiete)
                    # print(kaltmiete,'kaltmiete_dot_coma')
                elif ',' in kaltmiete_value:
                    kaltmiete = kaltmiete_value.replace(',' , '.')
                    kaltmiete = ''.join(kaltmiete) 
                    kaltmiete = float(kaltmiete)
                    # print(kaltmiete,'kaltmiete_coma')
                elif '.' in kaltmiete_value:
                    kaltmiete= kaltmiete_value.replace('.' , '')
                    kaltmiete = float(kaltmiete)
                    # print(kaltmiete,'kaltmiete_dot')
                
                    # print("Строка не содержит ни '.' ни ','")        
            except ValueError:
                # Обработка случая, когда строка не может быть преобразована в число
                kaltmiete = 0.0
            
            

            if nebenkosten_value is not None:
                nebenkosten = nebenkosten_value.replace(',', '.')
                nebenkosten = float(nebenkosten)
                nebenkosten = round(nebenkosten, 1)
                print(nebenkosten,"nebenkosten")
            else:
                nebenkosten = 0.0
            

            qm = qm_value.replace(',', '.') if qm_value else 0
            # print(f"kaltmiete: {kaltmiete}, nebenkosten: {nebenkosten}")


            # print("______Сложение (kaltmiete+nebenkosten) _________")
            gesammite = kaltmiete + nebenkosten
            print('Gesammite : ', gesammite)

            # print("______Сравнение по городам и их лимитам (locationFlat и gesammite), еще нужна квадратура до 50 квм. _________")
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
                if location_flat == city:
                # and gesammite <= value:
                    print("Город найден в списке:", city)
                    print("Соответствующее значение:", value,end="\n\n")
                    my_flat = MyFlat()
                    my_flat.test(city,gesammite, links_flat, nebenkosten, heizkosten_value)
                    my_flat.print_values()

                    break
                else:
                    print("Город не найден в списке.")
            
            print("Цикл закончился",end="\n\n")
                # param_location = param_flat[0][0]
                # param_gesammite = param_flat[0][1]
                # print(param_location,param_gesammite)     
                # and gesammite <= param_gesammite
                # if location_flat == param :
            #  and gesammite <= param_gesammite and qm <= 50.0:
                    # print(param, links_flat, location_flat,'==','Itzehoe', 'YES', qm)
            #     print('плюс дополнительные расходы', kaltmiete_zzgl_value )
            #     print("Heizkosten in Warmmiete enthalten", heizkosten_in_Warmmiete_enthalten, 'входит в Warmite')
            #     print("Heizkosten_nicht_in_Warmmiete_enthalten:", heizkosten_nicht_in_Warmmiete_enthalten, 'НЕвходит в Warmite')
            # elif links_flat == 'GlÃ¼ckstadt' and gesammite  >= 200.09 and qm <= 50.0:
            #     print(links_flat, 'Glücksstadt')
                # else:
                    # print('Hihyia nema')

except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
# finally:
#     if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
cursor.close()
print("Data successfully inserted into the database.")



# data = [
#     'https://www.immowelt.de/expose/2dx7g59',
#     'https://www.immowelt.de/expose/2c5e45z',
#     'https://www.immowelt.de/expose/2dgh258',
# ]