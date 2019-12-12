# Ebook Store PYDODBC Exercise 

This exercise is to consolidate the understanding of pyodbc and Python 

## TASK 

1. Create a new database in MS SQL 

2. Create one table with the columns: Title, Author, Date, Postcode, Lat, Long. 

3. Insert 5 books in the SQL Server

4. Connect to the project 

5. Have a function which retrieves all books and prints them with the following format

```
-> 1) title: XYZ - Author: XPTO - Date: 1/3/1343
-> 2) title: XYZ - Author: XPTO - Date: 1/3/1343
-> 3) title: XYZ - Author: XPTO - Date: 1/3/1343

```

6. Have a function which searches for a book title. 

7. Be able to insert a book (search for .commit())

8. Have an API method which allows you to add a postcode to a book 

9. Have a method called geo_code_api_call():
    - this method will get the postcode from a book, 
    - use the postcode to generate a URL (postcode.io)
    - use requests package to make a GET request added to the URL 
    - get the long and lat of the post code and print

10. Update the books with their long and lat 