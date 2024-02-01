import re
import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


data = [
    'https://www.immowelt.de/expose/2dx7g59',
    'https://www.immowelt.de/expose/2c5e45z',
    'https://www.immowelt.de/expose/2dgh258',
]

param_flat = [
['Itzehoe',454.25],['GlÃ¼ckstadt',445.09],
['Herzhorn',445.09], ['Horst',445.09],
['Krempe',411.68], ['Kremperheide',411.68],
['Wilster',411.68], ['Elmshorn',510.2],
['Pinneberg',559.2], ['Tornesh',559.2],
['Kiel',439]]
param_location = param_flat[0][0]
param_gesammite = param_flat[0][1]
print(param_location,param_gesammite)


    # Переменные для хранения значений
kaltmiete_value, nebenkosten_value, heizkosten_value, warmmiete_value, stellplatz_value,qm_value = [None] * 6
heizkosten_in_Warmmiete_enthalten, heizkosten_nicht_in_Warmmiete_enthalten = None, None


for links_prise_flat in data:
    print('_____________________________')
    sleep(2)
    url = f"{links_prise_flat}"
    print(links_prise_flat)

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # получаю квадратуру квартиры 
    qm = soup.find('span',class_ = 'has-font-300').get_text()
    qm_value = qm.split()[0] 
   
    # location_value = soup.find('sd-cell-col', class_='class="cell__col is-center-v')
    # print(f"location_value {location_value}")
    

    price_block = soup.find_all('sd-cell-row', class_='cell-size-100 cell__row ng-star-inserted')
    # print(price_block)
    
    prices_flat_data = []
 

    for tag in price_block:
        try:
            prise_flat = tag.get_text().replace('€', ' ').strip()
        except:
            prise_flat = 'Prise_flat_not_found'
        # print(prise_flat)
        prices_flat_data.append(prise_flat)
    print(prices_flat_data)


    for item in prices_flat_data:
        # Разделение строки по пробелу и получение последнего элемента
        value = item.split()[-1] 
        print('___________Разделение строки по пробелу__________________')
        print(value)
        # Проверка, к какой категории относится текущая строка и присвоение значения соответствующей переменной
        if 'Kaltmiete' in item:
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
    print('___________Вывод значений переменных__________________')
    print(f"Kaltmiete: {kaltmiete_value}")
    print(f"Nebenkosten:  {nebenkosten_value}")
    print(f"Heizkosten: {heizkosten_value}")
    print(f"Heizkosten in Warmmiete enthalten: {heizkosten_in_Warmmiete_enthalten}")
    print(f"Heizkosten_nicht_in_Warmmiete_enthalten: {heizkosten_nicht_in_Warmmiete_enthalten}")
    print(f"Warmmiete: {warmmiete_value}")
    print(f"Stellplatz: {stellplatz_value}")
    print(f"m² : {qm_value}")

    # сравнение происходит тут
    print("______Убрать точки в числах,в kaltmiete nebenkosten_________")
    kaltmiete = kaltmiete_value.replace('.', '') if kaltmiete_value else '0'
    nebenkosten = nebenkosten_value.replace('.', '') if nebenkosten_value else '0'
    print(f"kaltmiete: {kaltmiete}, nebenkosten: {nebenkosten}")
    print("______Сложение (kaltmiete+nebenkosten) _________")
    gesammite = float(kaltmiete) + float(nebenkosten)
    qm = float(qm_value)
    print('Gesammite : ', gesammite)
    print("______Сравнение по городам и их лимитам (locationFlat и gesammite), еще нужна квадратура до 50 квм. _________")
    if locationFlat == 'Itzehoe' and gesammite <= 5000.25 and qm <= 50.0:
        print(links_prise_flat, 'Itzehoe')
        print("Heizkosten in Warmmiete enthalten", heizkosten_in_Warmmiete_enthalten, 'входит в Warmite')
        print("Heizkosten_nicht_in_Warmmiete_enthalten:", heizkosten_nicht_in_Warmmiete_enthalten, 'НЕвходит в Warmite')
    elif locationFlat == 'GlÃ¼ckstadt' and gesammite == 445.09 and qm <= 50.0:
        print(links_prise_flat, 'GlÃ¼ckstadt')
    else:
        print('Hihyia nema')

print("Data successfully inserted into the database.")
