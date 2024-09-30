
import sqlite3


class DatabaseHandler:
 
    def __init__(self, db_name='allFlat.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_cursor(self, connection):
        return connection.cursor()
    
    def create_table(self, cursor):
         cursor.execute("CREATE TABLE IF NOT EXISTS allFlatsAfterParsoing1 (id INTEGER PRIMARY KEY AUTOINCREMENT,linkFlat TEXT, titleFlat TEXT, locationFlat TEXT, truePriceFlat TEXT, timeUpdate TEXT)")
         
    def delete_all_rows(self, cursor):
        cursor.execute("DELETE FROM allFlatsAfterParsoing1")

    def insert_data(self, cursor, data):
            cursor.execute("""
                INSERT INTO allFlatsAfterParsoing1 (linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate)
                VALUES (?, ?, ?, ?, ?)
            """, data)

    def update_all_rows(self,cursor, data):
        cursor.execute("""
        UPDATE allFlatsAfterParsoing1
        SET 
            titleFlat = ?,
            locationFlat = ?,
            truePriceFlat = ?,
            timeUpdate = ?
        WHERE linkFlat LIKE 'https%'
        """, data)
        
        
    #     # if cursor.rowcount == 0:
        #      # Если ни одна запись не была обновлена, то вставляем новую запись
        #     cursor.execute("""INSERT INTO allFlatsAfterParsoing1 (linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate)
        #                      VALUES (?, ?, ?, ?, ?)""", data)
        # else:
        #  print(f"Обновлено {cursor.rowcount} строк.")
      
  # def from_db_data(self,cursor):
    #     cursor.execute('''SELECT * FROM allFlatsAfterParsoing1 
    #             WHERE   titleFlat = ?, 
    #                     locationFlat = ?, 
    #                     truePriceFlat = ?,
    #                     linkFlat = ?''')

    # def add_time_update_column(self, cursor):
    #      cursor.execute("ALTER TABLE allFlatsAfterParsoing ADD COLUMN timeUpdate TEXT")
    # Попытка обновления существующей записи