from ebook_class import *
import pyodbc

table_ebooks = Ebook()

while True:
    print('_________________________________________')
    print('Option 1 -- Get all Books')
    print('Option 2 -- Search for a book')
    print('Option 3 -- Add a Book')
    print('Option 4 -- Add a Postcode')
    print('Option 5 -- Add Longitude and Latitude to a Book')
    print("'exit to close the program'")

    print('_________________________________________')


    user_input = input('Please choose a number from the options listed...')
    print('_________________________________________')

    if user_input == '1':
        print('Getting all Books...')
        table_ebooks.get_all_books()

    elif user_input == '2':
        table_ebooks.search_ebook()

    elif user_input == '3':
        print('We need some information to add a new book in!')
        table_ebooks.add_ebook()
        print('Book has been added!')

    elif user_input == '4':
        table_ebooks.add_postcode_to_book()
        print('Postcode has been added!')

    elif user_input == '5':
        table_ebooks.geo_code_api_call()
        print('Longitude and Latitude added to chosen postcode')

    else:
        break
    print('Thank you, you have exited!')