from app import db, app
from project.books.model import Books
from project.customers.model import Customers
from project.loans.model import Loans
import datetime



book_1 = Books(name = "The Red Scarf", Author = "Ram Oren", Year_published = "2013", Type = 1, Image="red_scarf.jpg")
book_2 = Books(name = "Orphan Train", Author = "Christina Baker Kline", Year_published = "2013", Type = 2, Image="train.jpg")
book_3 = Books(name = "The Lost Flowers Of Alice Hart", Author = "Holly Ringland", Year_published = "2018", Type = 3, Image="flowers.jpg")

customer_1 = Customers(name = "Yhel Ruff", city = "Hiran", age = 8)
customer_2 = Customers(name = "Avital Reznik", city = "Ariel", age = 48)
customer_3 = Customers(name = "Drora Altman", city = "Jerusalem", age = 46)


loan_1 = Loans(CustID = 1, BookID = 1, Loandate = datetime.datetime.strptime('2022-11-01', '%Y-%m-%d'), Returndate = datetime.datetime.strptime('2022-11-11', '%Y-%m-%d'),returned= True)
loan_2 = Loans(CustID = 2, BookID = 2, Loandate = datetime.datetime.strptime('2022-11-08','%Y-%m-%d'), Returndate = datetime.datetime.strptime('2022-11-13', '%Y-%m-%d'),returned= True)
loan_3 = Loans(CustID = 3, BookID = 3, Loandate = datetime.datetime.strptime('2022-11-15','%Y-%m-%d'), Returndate = datetime.datetime.strptime('2022-11-17', '%Y-%m-%d'),returned= True)


with app.app_context():
    db.create_all()
    db.session.add_all([book_1, book_2, book_3])
    db.session.add_all([customer_1, customer_2, customer_3])
    db.session.add_all([loan_1, loan_2, loan_3])
    db.session.commit()