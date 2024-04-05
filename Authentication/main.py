from flask import request 
from flask_login import LoginManager, login_user, logout_user, current_user
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
    if current_user.is_authenticated:
        clearance = current_user.clearance
        return f"{clearance}", 200
    else:
        return "User not authenticated", 401


@app.route('/login', methods=['POST'])
def login():
    user = Users.query.filter_by(username=request.form.get("username")).first()
    if user and user.password == request.form.get("password"):
        login_user(user)
        return "Logged in successfuly", 200
    else:
        return "something went wrong", 401

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    clearance = request.form.get('clearance')
    new_user = Users(username=username, password=password, clearance=clearance)
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