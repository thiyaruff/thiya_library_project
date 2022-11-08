from project import app, db


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    city=db.Column(db.String(15))
    age=db.Column(db.Integer)
    loans= db.relationship('Loans',backref='customers', lazy=True)

    def __init__(self,name,city,age):
        self.name=name
        self.city=city
        self.age=age

