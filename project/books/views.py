

from project import app,db
from flask import Blueprint, redirect,request,render_template
from project.books.model import Books
from project.loans.model import Loans



books = Blueprint('books', __name__, template_folder='template')


# display all the book in the liberary
@books.route("/all_books/")
def all_books():
    return render_template('all_books.html',books= Books.query.all()) 

# find one book from the book list, search by name
@books.route("/book/" , methods=['POST','GET'])
def search_book():
    global book1
    if request.method=='POST':
        books=Books.query.all()
        for book in books:
            if book.name==request.form.get("name"):
                book1=book
                return render_template('book.html',book1=book1)
    else:        
        return render_template('book.html',)
        
     


# add a book to the list
@books.route("/add_book/", methods=['POST','GET'])
def add_book():
    global new_book
    if request.method=='POST':
        new_book= request.form
        newBook= Books(new_book['name'],new_book['Author'],new_book['Year_published'],new_book['Type'],new_book['Image'])
        db.session.add (newBook)
        db.session.commit()
        alert= "a new book add to the library list"
        return render_template('add_book.html',alert= alert)
    return render_template('add_book.html')


# delete book from the library
@books.route("/del_book/<id>", methods=['DELETE','GET'])
def del_book(id=-1):
    book=Books.query.get(int(id))
    if book:
        loans = Loans.query.filter_by(returned = False)
        for loan in loans:
            if book.id == loan.books_id:
                return render_template('all_books.html', books = Books.query.all(), active_loan = True)
        db.session.delete(book)
        db.session.commit()
        return render_template('all_books.html',books = Books.query.all())





        
