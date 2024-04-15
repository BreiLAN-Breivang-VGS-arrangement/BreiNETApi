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
    return "Tournament created", 200

@app.route('/delete_tournament/<int:tournament_id>', methods=['DELETE'])
def delete_tournament(tournament_id):
    tournament = Tournaments.query.get(tournament_id)

    if not tournament:
        return "Tournament does not exist", 400
    else:
        db.session.delete(tournament)
        db.session.commit()
        return "Tournament deleted", 200

@app.route('/update_tournament/<int:tournament_id>', methods=['PATCH'])
def update_tournament(tournament_id):
    tournament = Tournaments.query.get(tournament_id)
    
    if not tournament:
        return "A tournament with the given id does not exist", 400
    
    data = request.form
    tournament.name = data.get("firstName", tournament.name)
    tournament.time = data.get("lastName", tournament.time)
    tournament.date = data.get("email", tournament.date)
    tournament.host = data.get("email", tournament.host)
    tournament.link = data.get("email", tournament.link)
    
    db.session.commit()

    return "Tournament successfully modified", 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0", port="5001")