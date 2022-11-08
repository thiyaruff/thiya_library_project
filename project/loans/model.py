from project import app, db


class Loans(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    CustID = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    BookID = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    Loandate = db.Column(db.Date, nullable=False)
    Returndate=db.Column(db.Date, nullable=False)
    returned = db.Column(db.Boolean,default=False)

    def __init__(self, CustID,BookID, Loandate,Returndate,returned):
        self.CustID=CustID
        self.BookID=BookID
        self.Loandate=Loandate
        self.Returndate = Returndate
        self.returned=returned
    

