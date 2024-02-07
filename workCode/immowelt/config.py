import notification_bot
class MyFlat:
    def test(self, city,gesammite, links_flat, nebencosten, heizkosten_value):
        self.city = city
        self.gesammite = gesammite
        self.links_flat = links_flat
        self.nebencosten = nebencosten
        self.heizkosten_value = heizkosten_value
    
    def print_values(self):
        print("City:", self.city)
        print("Gesammite:", self.gesammite)
        print("Links Flat:", self.links_flat)
        print("Nebenkosten:", self.nebencosten)
        print("Heizkosten Value:", self.heizkosten_value)
        notification_bot.notification(self.city, self.gesammite, self.links_flat, self.nebencosten, self.heizkosten_value)

# my_object = MyFlat(city, gesammite, links_flat, nebenkosten, heizkosten_valu)


# sleep(3)







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
