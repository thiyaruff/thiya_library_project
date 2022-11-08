import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_library.sqlite3'
app.config['SECRET_KEY'] = "random string"




db = SQLAlchemy(app)

from project.core.views import home
from project.books.views import books
from project.customers.views import customers
from project.loans.views import loans

app.register_blueprint(home)
app.register_blueprint(books)
app.register_blueprint(customers)
app.register_blueprint(loans)