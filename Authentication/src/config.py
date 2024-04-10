from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import platform, sys, os

app = Flask(__name__)
CORS(app, resources={r"/login": {"origins" : "http://localhost:5173"}})

# Function to automatically adjust path to database on systems like, windows, arch, and debian etc.
"""
def database_URI():
    operatingSystem = platform.system()
    match operatingSystem:
        case 'Windows':
            print(f"running on {operatingSystem}", file=sys.stderr)
            return 'sqlite:///database.sqlite'
        case _ :
            print(f"running on {operatingSystem}", file=sys.stderr)
            return 'sqlite:////database.sqlite'
"""        


current_dir = os.path.abspath(os.path.dirname(__file__))
database_file = os.path.join(current_dir, '../instance/database.sqlite')


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'My-secret-key'

db = SQLAlchemy(app)