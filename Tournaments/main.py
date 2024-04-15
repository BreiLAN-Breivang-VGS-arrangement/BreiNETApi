from flask import request, jsonify
from src.config import app, db
from src.models import Tournaments
import requests

with app.app_context():
    db.create_all()

@app.route('/fetchtourney', methods=['GET'])
def fetchtourney():
    tournaments = Tournaments.query.all()
    json_tournaments = list(map(lambda x: x.to_json(), tournaments))
    return jsonify({"tournaments": json_tournaments})

@app.route('/createtourney', methods=['POST'])
def Create_Tournament():
    name = request.form.get('name')
    time = request.form.get('time')
    date = request.form.get('date')
    host = request.form.get('host')
    link = request.form.get('link')
    new_tourney = Tournaments(name=name, time=time, date=date, host=host, link=link)
    db.session.add(new_tourney)
    db.session.commit()
    return "Tournament created", 418

@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_tournament(user_id):
        

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0", port="5001")