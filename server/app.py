# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    # query the database for an earthquake with this id
    earthquake = Earthquake.query.filter_by(id=id).first()

    # if no earthquake is found, return a 404 error
    if earthquake is None:
        return {"message": f"Earthquake {id} not found."}, 404

    # return the earthquake data as JSON
    return {
        "id": earthquake.id,
        "location": earthquake.location,
        "magnitude": earthquake.magnitude,
        "year": earthquake.year
    }, 200

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    # query earthquakes with magnitude greater than or equal to the given value
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # build a list of earthquake data
    quakes = []
    for earthquake in earthquakes:
        quakes.append({
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        })

    # return the count and the list of earthquakes
    return {
        "count": len(quakes),
        "quakes": quakes
    }, 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
