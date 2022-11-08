
import datetime
from project import app,db
from flask import Blueprint
from flask import request,render_template
from project.loans.model import Loans
from project.books.model import Books
from project.customers.model import Customers




loans = Blueprint('loans', __name__, template_folder='template')


#new loan
@loans.route("/new_loan/", methods=['POST','GET'])
def new_loan():
    alert="None"
    if request.method=='POST':
        current_book=db.session.query(Books).filter_by(id=int(request.form.get("books"))).first()
        if db.session.query(Loans).filter_by(BookID=current_book.id).first():
            alert="Book is allready lent"
        else:
            if current_book.Type==1:
                return_date=datetime.date.today()+datetime.timedelta(days=10)
            elif current_book.Type==2:
                return_date=datetime.date.today()+datetime.timedelta(days=5)
            else:
                return_date=datetime.date.today()+datetime.timedelta(days=2)
                # returned=True
            newLoan=Loans(request.form.get("customers"),request.form.get("books"),datetime.date.today(),return_date,returned=True)
            db.session.add(newLoan)
            db.session.commit()
            alert="new loan success"
    return render_template('new_loan.html',books=Books.query.all(),customers=Customers.query.all(),loans = Loans.query.filter_by(returned = False),alert=alert)
          

# return book to the library
@loans.route("/return_loan/<id>", methods = ['GET','DELETE'])
def delete_loan(id=-1): 
    loan = Loans.query.get (int(id))
    if loan.returned == True:
        db.session.delete(loan)
        db.session.commit()
        return render_template('all_loans.html', loan = loans,alert="the book return to the library")
    # else:
    #     return render_template('all_loans.html')

# display all loans
@loans.route("/all_loans/", methods = ['GET'])
def all_loans():
    return render_template('all_loans.html',loans=Loans.query.all())

# show all late loans
@loans.route('/late_loans/', methods = ['GET'])
def late_loans():
    late_loans = []
    loans = Loans.query.all()
    for loan in loans:
            if loan.Returndate < datetime.date.today():
                late_loans.append(loan)
    return render_template ("late_loans.html", late_loans = late_loans)