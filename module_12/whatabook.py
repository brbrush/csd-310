## Project Title: whatabook.py
## Author: Brandon Brush
## Date: February 21, 2022
## Description: Whatabook supply and account manager for users

import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

##Testing Connection
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config['user'], config['host'], config['database']))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")   
    elif err.errno == errorcode.ER_BAD_DB-ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

cursor = db.cursor()

##Main menu navigation
def showmenu():
    print("\nMenu\n\n  1. View Books\n  2. View Store Locations\n  3. My Account\n  4. Exit Program\n")
    _cursor = int(input("Please make a selection: "))
    while _cursor < 1 or _cursor > 4:
        print("\nInvalid Selection.")
        _cursor = int(input("\nPlease Make a Selection: "))
    return _cursor

##Displays all books
def show_books():
    cursor.execute("SELECT book_id, book_name, author, details FROM book;")
    doc = cursor.fetchall()
    print("\n-- DISPLAYING BOOK CATALOGUE --")
    for docs in doc:
        print("Book ID: {}".format(docs[0]), "\nBook Name: {}".format(docs[1]), "\nAuthor: {}".format(docs[2]), "\nDetails: {}\n".format(docs[3]))

##Displays all locations
def show_locations():
    cursor.execute("SELECT store_id, locale FROM store;")
    doc = cursor.fetchall()
    print("\n-- DISPLAYING ALL LOCATIONS --")
    for docs in doc:
        print("Store ID: {}".format(docs[0]), "\nLocation: {}".format(docs[1]))

##User account menu
def show_account_menu():
    _cursor = 0
    while _cursor !=4:
        print("\nAccount Menu:\n  1. Display Wishlist\n  2. Add Book from Wishlist\n  3. Delete Book from Wishlist\n  4. Return to Main Menu")
        _cursor = int(input("\nPlease Make a Selection: "))
        if _cursor == 1:
            show_wishlist(_user_id)
            continue
        elif _cursor == 2:
            show_books_to_add(_user_id)
            add_book_to_wishlist(_user_id)
            continue
        elif _cursor == 3:
            delete_book_from_list(_user_id)
            continue
        elif _cursor == 4:
            print("")
        while _cursor < 1 or _cursor > 5:
            print("\nInvalid Selection.")
            _cursor = int(input("\nPlease Make a Selection: "))

##Validating user account exists
def validate_user():
    _user_id = str(input("\nPlease Enter User ID: "))
    cursor.execute("SELECT user_id, first_name FROM user WHERE user_id = " + _user_id + ";")
    doc = cursor.fetchone()
    if doc == None:
        print("\nUser ID not found, please try again.")
        validate_user()
    else: 
        print("\nWelcome {}:".format(doc[1])"\nPlease exit program to log out")
        return _user_id

##Displays current wishlist
def show_wishlist(_user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id where user.user_id = " + _user_id + ";")
    doc = cursor.fetchall()
    print("\n-- DISPLAYING CURRENT WISHLIST --")
    for docs in doc:
        print("Book ID: {}".format(docs[3]), "\nBook Name: {}".format(docs[4]), "\nAuthor: {}".format(docs[5]), "\nDetails: {}\n".format(docs[6]))

##Displays books not currently in wishlist
def show_books_to_add(_user_id):
    cursor.execute("SELECT book.book_id, book.book_name, book.author, book.details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id =" + _user_id + ");")
    doc = cursor.fetchall()
    print("\n-- DISPLAYING AVAILABLE BOOKS TO ADD WISHLIST --")
    for docs in doc:
        print("Book ID: {}".format(docs[0]), "\nBook Name: {}".format(docs[1]), "\nAuthor: {}".format(docs[2]), "\nDetails: {}\n".format(docs[3]))

##Delete from wishlist
def delete_book_from_list(_user_id):
    _book_id = int(input("\nEnter Book ID to Remove from List: "))
    try:
        cursor.execute("DELETE FROM wishlist WHERE user_id = " + str(_user_id) + " AND book_id = " + str(_book_id) + ";")
    except mysql.connector.Error as err:
        print("Error Occurred, Please Try Again")

##Add to wishlist
def add_book_to_wishlist(_user_id):
    _book_id = int(input("\nSelect Book to Add: "))
    try:
        cursor.execute("INSERT INTO wishlist(user_id, book_ID) VALUES(" + str(_user_id) + ", " + str(_book_id) + ");")
    except mysql.connector.Error as err:
        print("Error Occurred, Please Try Again")

_user_id = 0
##Program/Menu Loop
while True:
    _cursor = showmenu()
    if _cursor == 1:
        show_books()
    elif _cursor == 2:
        show_locations()
    elif _cursor == 3:
        if _user_id != 0:
            show_account_menu()
        else:
            _user_id = validate_user()
            show_account_menu()
    elif _cursor == 4:
        db.close()
        quit()
    continue