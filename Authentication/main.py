from flask import request, jsonify, Flask
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from config import app, db
from models import Users


login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

@app.route('/checkauth', methods=['GET'])
def Check_auth():
    if current_user.is_authenticated:
        return "user is authenticated", 200
    else:
        return "user not authenticated", 401
    
@app.route('/privilegecheck', methods=['GET'])
def check_privilege():
    pass

@app.route('/login', methods=['POST'])
def login():
    user = Users.query.filter_by(username=request.form.get("username")).first()
    if user and user.password == request.form.get("password"):
        login_user(user)
        return "Logged in successfuly", 200
    else:
        return "something went wrong", 401

@app.route('/adduser', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    new_user = Users(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return "user created", 418

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return "user logged out", 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0")