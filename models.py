import flask_sqlalchemy
import uuid
from sqlalchemy import Boolean, Column, DateTime, Date, Float, ForeignKey, Integer, JSON, PickleType, Text, Table, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask_login import LoginManager, UserMixin

db = flask_sqlalchemy.SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))
    age = db.Column(db.DateTime)
    ownerId = db.Column(db.String(100))

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Locations(db.Model):
    __tablename__ = 'locations'
    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(), unique=True, nullable=False)

class Rooms(db.Model):
    __tablename__ = 'rooms'
    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    locationID = db.Column(db.String(), db.ForeignKey('locations.id'), nullable=False)
    #id = db.Column(db.Integer, primary_key=True)
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(64), unique=True)
    #default = db.Column(db.Boolean, default=False, index=True)
    # def __init__(self, id, name, location):
    #   self.id = id
    #   self.name = name
    #   self.location = location

class Staffs(db.Model):
    __tablename__ = 'staffs'
    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)

class Bookings(db.Model):
    __tablename__ = 'bookings'
    #id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4, unique=True)
    staffID = db.Column(db.String(), db.ForeignKey('staffs.id'), nullable=False)
    roomID = db.Column(db.String(), db.ForeignKey('rooms.id'), nullable=False)
    starttime = db.Column(db.DateTime, nullable=False)
    endtime = db.Column(db.DateTime, nullable=False)
    eventdate = db.Column(db.Date, nullable=False)
    booktime= db.Column(db.DateTime, default=datetime.now)

    # def __init__(self, title, text):
    #     self.title = title
    #     self.text = text
    #     self.done = False
    #     self.pub_date = datetime.utcnow()
#   def __init__(self, id, staff, room, starttime, endtime):
#     self.id = id
#     self.staff = staff
#     self.room = room
#     self.starttime = starttime
#     self.endtime = endtime
#   def getID(self):
#     print("Hello my name is " + str(self.id))


# class Room(db.Model):
#   __tablename__ = 'Room'
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String())
#   location = db.Column(db.String())
#   #result_no_stop_words = db.Column(JSON)
#   def __init__(self, id, name, location):
#     self.id = id
#     self.name = name
#     self.location = location
#   def getName(self):
#     print("Hello my name is " + self.name)

# class Staff(db.Model):
#   def __init__(self, id, name, email):
#     self.id = id
#     self.name = name
#     self.email = email
#   def getName(self):
#     print("Hello my name is " + self.name)

# class Booking(db.Model):
#   def __init__(self, id, staff, room, starttime, endtime):
#     self.id = id
#     self.staff = staff
#     self.room = room
#     self.starttime = starttime
#     self.endtime = endtime
#   def getID(self):
#     print("Hello my name is " + str(self.id))
