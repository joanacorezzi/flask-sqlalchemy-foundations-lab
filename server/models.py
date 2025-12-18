from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here

# Earthquake model
class Earthquake(db.Model):
    # table name
    __tablename__ = "earthquakes"

    # primary key
    id = db.Column(db.Integer, primary_key=True)

    # magnitude of the earthquake
    magnitude = db.Column(db.Float)

    # location of the earthquake
    location = db.Column(db.String)

    # year the earthquake happened
    year = db.Column(db.Integer)

    # string representation of the object
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"