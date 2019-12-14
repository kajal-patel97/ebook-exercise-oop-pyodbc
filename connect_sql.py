# Need to import pyodbc

import pyodbc

class MSDBConnection():

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'ebook_store'
        self.user_name = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_ebook_store = pyodbc.connect( 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.user_name + ';PWD=' + self.password)

        self.cursor = self.docker_ebook_store.cursor()

    def __sql_query(self,sql_query):
        return self.cursor.execute(sql_query)