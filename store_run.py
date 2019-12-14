from ebook_class import *
import pyodbc

table_ebooks = Ebook()

while True:
    print('_________________________________________')
    print('Option 1 -- Get all Books')




    print('_________________________________________')
    user_input = input('Please choose a number from the options listed...')
    print('_________________________________________')

    if user_input == '1':
        print('Getting all Books...')
        table_ebooks.get_all_books()
