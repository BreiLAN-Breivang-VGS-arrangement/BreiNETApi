from flask import request, jsonify, Flask
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from config import app, db
from models import Users


login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user():
    return db.session.get(Users, user_id)

@app.route('/checkauth', methods=['POST'])
def Check_auth():
    pass


@app.route('/login', methods=['POST'])
def login():
    pass

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0")