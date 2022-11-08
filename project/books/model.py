from project import app, db

class   Books(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    Author=db.Column(db.String(15))
    Year_published=db.Column(db.Integer)
    Type=db.Column(db.Integer)
    Image=db.Column(db.String(50),default="book.png")
    loans= db.relationship('Loans',backref='books', lazy=True)
    def __init__(self, name,Author,Year_published,Type, Image):
        self.name = name
        self.Author = Author
        self.Year_published = Year_published
        self.Type = Type
        self.Image=Image
       

