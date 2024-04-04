from flask import Flask, url_for
from flask_cors import CORS
import sqlalchemy

from .model.user import user

mod: user = user(0,"admin",123,False)

app = Flask(__name__)
CORS(app)

@app.route('/',methods=["GET"])
def root() -> str:
    return "hello world"

@app.route('/admin')
def admin():
    pass

@app.route('/login',methods=["GET","POST"])
def login():
    pass

@app.before_request(url_for('admin'))
def loginState() -> bool:
    if mod.loginState == False:
        return Flask.redirect(url_for('login'))
    elif mod.loginState == True:
        pass