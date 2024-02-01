
from time import sleep


class my_flat:
    def __init__(self, title, nebencosten,location,kaltmiete,heizkosten):
        self.title = title
        self.nebencosten = nebencosten
        self.location = location
        self.kaltmiete = kaltmiete
        self.heizkosten = heizkosten

 
  

my_object = my_flat('Super Flat','100','Izehoe','300','50')
print(my_object.title)  
print(my_object.nebencosten)

sleep(3)







# # host = "127.0.0.1"
# # user= "root"
# # password = "lolkek123"
# # db_name = ""
# import sqlite3
# import simpleParser

# def writeDB():
# # Подключаемся к базе данных
#     db = sqlite3.connect('allFlat.db')

# # Создаем объект курсора
#     c = db.cursor()

# # Добавление данных
#     c.execute("""
#         INSERT INTO allFlatsAfterParsoing (linkFlat, titleFlat, locationFlat, truePriceFlat)
#         VALUES (?, ?, ?, ?)
#     """, (simpleParser.linkFlat, 
#           simpleParser.titleFlat, 
#           simpleParser.locationFlat, 
#           simpleParser.truePriceFlat))

# # Изменение данных
#     c.execute("""
#         UPDATE allFlatsAfterParsoing
#         SET
#             linkFlat = ?,
#             titleFlat = ?,
#             locationFlat = ?,
#             truePriceFlat = ?
#     """, (simpleParser.linkFlat, 
#           simpleParser.titleFlat, 
#           simpleParser.locationFlat, 
#           simpleParser.truePriceFlat))
    

# # Применяем изменения
#     db.commit()

# # Закрываем соединение
#     db.close()



# c.execute(""" CREATE TABLE allFlatsAfterParsoing (
#     linkFlat text,
#     titleFlat text, 
#     locationFlat text,
#     truePriceFlat text
# )""")


# Добавление данн
# c = db.execute("INSERT INTO allFlatsAfterParsoing VALUES(linkFlat,titleFlat,locationFlat,truePriceFlat)")

# Вывод данн
# c = db.execute("SELECT * FROM allFlatsAfterParsoing")
# c = db.execute("SELECT linkFlat FROM allFlatsAfterParsoing") будут только ссылки выводиться
# c = db.execute("SELECT rowid, linkFlat FROM allFlatsAfterParsoing") будут только ссылки выводиться c уникальным идентификатором

# print(c.fetchall()) # команда помогает вывести все записи
#print(c.fetсhmany(1)) # команда помогает вывести кол-во записей
#print(c.fetсhone(1)) # команда помогает вывести только одну запись
