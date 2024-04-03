from config import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(40), unique=True, nullable=False)
    password = db.Column(db.string(120), nullable=False)
    role = db.Column(db.string(80), unique=False, nullable=False)