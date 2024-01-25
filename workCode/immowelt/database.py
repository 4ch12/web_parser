import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='allFlat.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_cursor(self, connection):
        return connection.cursor()

    def create_table(self, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS allFlatsAfterParsoing (linkFlat TEXT, titleFlat TEXT, locationFlat TEXT, truePriceFlat TEXT)")

    def delete_all_rows(self, cursor):
        cursor.execute("DELETE FROM allFlatsAfterParsoing")

    def insert_data(self, cursor, data):
        cursor.executemany("""
            INSERT INTO allFlatsAfterParsoing (linkFlat, titleFlat, locationFlat, truePriceFlat)
            VALUES (?, ?, ?, ?)
        """, data)

