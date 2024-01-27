import sqlite3



class DatabaseHandler:
 
    def __init__(self, db_name='allFlat.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_cursor(self, connection):
        return connection.cursor()

    # def create_table(self, cursor):
    #     cursor.execute("CREATE TABLE IF NOT EXISTS allFlatsAfterParsoing (linkFlat TEXT, titleFlat TEXT, locationFlat TEXT, truePriceFlat TEXT, timeUpdate DATETIME)")

    # def add_time_update_column(self, cursor):
    #     cursor.execute("ALTER TABLE allFlatsAfterParsoing ADD COLUMN timeUpdate TEXT")

    #  def delete_all_rows(self, cursor):
    #cursor.execute("DELETE FROM allFlatsAfterParsoing")
  

  # Попытка обновления существующей записи
    def update_all_rows(self, cursor, data):
        cursor.execute('''UPDATE allFlatsAfterParsoing
            SET titleFlat = ?, locationFlat = ?, truePriceFlat = ?, timeUpdate = ?
            WHERE linkFlat = ?''', data)

        if cursor.rowcount == 0:
            # Если ни одна запись не была обновлена, то вставляем новую запись
            cursor.execute('''INSERT INTO allFlatsAfterParsoing (linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate)
                            VALUES (?, ?, ?, ?, ?)''', data)

    # def insert_data(self, cursor, data):
    #     cursor.executemany("""
    #         INSERT INTO allFlatsAfterParsoing (linkFlat, titleFlat, locationFlat, truePriceFlat, timeUpdate)
    #         VALUES (?, ?, ?, ?, ?)
    #     """, data)
