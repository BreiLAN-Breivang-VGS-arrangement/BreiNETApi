from flask import request, jsonify
from config import app, db
from models import Contacts

@app.route('/Authentication')
def method_name():
    users = Users.query.all()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0")
