
# thiya_project blueprint_upload

my project is a management software to library.
the librarian can add books,customers,manage the loans etc.


## before running the program
first start with install virtualenviroment to your computer
$ pip install virtualenv
$ py -m virtualenv myenv

then install the packages in the requirments.exe file:
$ pip install -r requirements.txt

## db tables
there are three db tables in the program:
* books
* customer
* loans
you can find each of them in the files calls "model" under the relevant folder (books,customers,loans)

## init_db
this program has init_db file' so you can initialize the database cluster's default locale.
by start running in the terminal:
 $ py init_db

## start running the program

$ py app

## blueprint

the program bild with blueprint:
* "home" in "core" folder - the layout and the hompage
* "books" in "books" folder- all the books functions:
   - add a book
   - display all books
   - delete a book
   - search a book by name
* "customers" in "customers" folder- all the customers functions:
  - add a customer
  - display all customers
  - delete a customer 
  - search a customer by name
* "loans" in  "loans" folder - all the loan functions:
  - new loan
  - display all loans
  - late loans (to check late lone you can change the return_date in the function new_loan by add '+datetime.timedelta(days=-10)' to the 'return_date' )
  - delete loan (return a book)

## Author

- Thiya (Mushy) Ruff

