from project import app,db
from flask import Blueprint
from flask import request,render_template
from project.customers.model import Customers
from project.loans.model import Loans


customers = Blueprint('customers', __name__, template_folder='template')

# add a new customer to the library
@customers.route("/add_customer/", methods=['POST','GET'])
def add_customer():
    if request.method=='POST':
        new_customer=request.form
        newcust=Customers(new_customer['name'],new_customer['city'],new_customer['age']) 
        db.session.add (newcust)
        db.session.commit()
        return render_template ('add_customer.html',alert="a new customer add")
    return render_template ('add_customer.html')

# display all the customers in the library
@customers.route("/all_customers/<name>",methods=['GET'])
@customers.route("/all_customers/")
def display_all_customer():
    return render_template('all_customers.html',customers= Customers.query.all())

# delete customer from the library
@customers.route("/del_cust/<id>", methods=['DELETE','GET'])
def del_customer(id=-1):
    customer = Customers.query.get(id)
    if customer: 
        loans = Loans.query.filter_by(returned = False)
        for loan in loans:
            if customer.id == loan.CustID:
                alert="this customer have loan,cannot delete"
                return render_template('all_customers.html', customers = Customers.query.all(), active_loan = True,alert=alert)
        db.session.delete(customer)
        db.session.commit()
        return render_template('all_customers.html', customers = Customers.query.all()) 

# find one customer from the customer list, search by name
@customers.route("/customer/" , methods=['POST','GET'])
def search_customer():
    global customer1
    if request.method=='POST':
        customers = Customers.query.all()
        for customer in customers:
            if customer.name==request.form.get("name"):
                customer1=customer
                return render_template('customer.html',customer1=customer)
    else:        
        return render_template('customer.html')