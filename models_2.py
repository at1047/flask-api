import flask_sqlalchemy


db = flask_sqlalchemy

class Cats(db.model):
    __tablename__ = 'Cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    price = db.Column(db.Integer)
    age = db.Column(db.DateTime)

class Rooms(db.model):
    __tablename__ = 'Rooms'

class Location(db.model):
    __tablename__ = 'Locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), )
