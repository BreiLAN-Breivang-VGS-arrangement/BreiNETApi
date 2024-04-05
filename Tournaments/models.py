from config import db

class Tournaments(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    time = db.Column(db.String(40), unique=False, nullable=False)
    date = db.Column(db.DATE, unique=False, nullable=False)
    host = db.Column(db.String, unique=False, nullable=False)
    link = db.Column(db.String, unique=False, nullable=False)