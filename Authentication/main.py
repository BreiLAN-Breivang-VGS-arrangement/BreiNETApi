from flask import request, session
from flask_login import LoginManager
from src.config import app, db
from src.models import Users
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


def Check_auth():
    if session.get('username') != None:
        return True
    else:
        return False

@app.route('checkauth', methods=['GET'])
def send_auth():
    pass

@app.route('/privilegecheck', methods=['GET'])
def check_privilege():
    if Check_auth():
        username = session.get('username')
        user = Users.query.filter_by(username=username).first()
        clearance = user.clearance
        return f"{clearance}", 200
    else:
        return "User not authenticated", 401


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    user = Users.query.filter_by(username=username).first()
    password = request.form.get("password")
    if check_password_hash(user.password, password):
        session['username'] = username
        return "Logged in successfuly", 200
    else:
        return "something went wrong", 401

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = generate_password_hash(request.form.get('password'))
    clearance = request.form.get('clearance')
    new_user = Users(username=username, password=password, clearance=clearance)
    db.session.add(new_user)
    db.session.commit()
    return "user created", 418

@app.route('/logout', methods=['POST'])
def logout():
    if Check_auth():
        session.pop('username', None)
        return "user logged out", 200
    else:
        return "not logged in", 401

@app.route('/currentuser', methods=['GET'])
def currentuser():
    if Check_auth():
        return f"{session.get('username')}", 200
    else:
        return "No user authenticated in current session", 401
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0")