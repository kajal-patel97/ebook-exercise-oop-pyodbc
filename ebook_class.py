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

    def search_ebook(self):
        ask_book = input('What is the name of your book?')
        query = f"SELECT * FROM ebooks WHERE title LIKE '%{ask_book}%'"
        result = self._MSDBConnection__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(record)
        return 'All Books Listed'