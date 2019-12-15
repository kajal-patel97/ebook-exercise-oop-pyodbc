import pyodbc
from connect_sql import *
import requests

class Ebook(MSDBConnection):

    def get_all_books(self):
        query = "SELECT * FROM ebooks"
        result = self._MSDBConnection__sql_query(query)

        while True:
            record = result.fetchone()
            if record is None:
                break
            print(f"ID:{record.ebook_id}- Title: {record.title} - Author: {record.author} - Date: {record.date_published}")
        print('All Records Retrieved')

    def search_ebook(self):
        ask_book = input('What is the name of your book?')
        query = f"SELECT * FROM ebooks WHERE title LIKE '%{ask_book.title()}%'"
        result = self._MSDBConnection__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(
                f"Title: {record.title} - Author: {record.author} - Genre: {record.genre} - Date Published: {record.date_published} - Postcode: {record.postcode} - Longitude/Latitude: {record.longitude}/{record.latitude}")
        print('All Books Listed')

    def add_ebook(self):
        ask_title = input('What is the title of the book you would like to add?')
        ask_author = input('What is the Author of this book?')
        ask_genre = input('What genre does this book come under?')
        ask_date_year = input('What year was this published in? (please user numerical values)')
        ask_date_month = input('What month was the book published (please user numerical values)')
        ask_date_day = input('Finally what day was this book published? (please user numerical values)')
        query = f"INSERT INTO ebooks (title, author, genre, date_published) VALUES ('{ask_title.title()}', '{ask_author.title()}', '{ask_genre.title()}', '{ask_date_year}-{ask_date_month}-{ask_date_day}')"
        result = self._MSDBConnection__sql_query(query)
        self.docker_ebook_store.commit()
        return result

    def add_postcode_to_book(self):
        postcode = input('Whats the postcode you want to add?').upper()
        id = input('What is the ebook id you would like to add this to..')
        query = f"UPDATE ebooks SET postcode ='{postcode}' WHERE ebook_id = '{id}'"
        result = self._MSDBConnection__sql_query(query)
        self.docker_ebook_store.commit()
        return result

    def geo_code_api_call(self):
        get_id = input('What is the book ID you would like to get a postcode for?')
        get_postcode = f"SELECT postcode FROM ebooks WHERE ebook_id = '{get_id}'"
        result = self._MSDBConnection__sql_query(get_postcode)
        while True:
            record = result.fetchone()
            if record is None:
                break
            postcode = record.postcode

        #build a URL
        path_url = 'http://api.postcodes.io/postcodes/'
        arg = f'{postcode}'
        post_code = requests.get(path_url + arg.strip())

        #turn into a dictionary
        post_code_dictionary = post_code.json()

        #get the information
        long = post_code_dictionary['result']['longitude']
        lat = post_code_dictionary['result']['latitude']

        #input into data base

        query = f"UPDATE ebooks SET longitude = '{long}', latitude = '{lat}' WHERE ebook_id = {get_id}"
        result2 = self._MSDBConnection__sql_query(query)
        self.docker_ebook_store.commit()

        return result2
