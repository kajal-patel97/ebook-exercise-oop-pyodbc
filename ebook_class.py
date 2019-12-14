import pyodbc
from connect_sql import *

class Ebook(MSDBConnection):

    def get_all_books(self):
        query = "SELECT * FROM ebooks"
        result = self._MSDBConnection__sql_query(query)

        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f"Title: {record.title} - Author: {record.author} - Date: {record.date_published}")
        print('All Records Retrieved')