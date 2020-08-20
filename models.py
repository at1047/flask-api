import flask_sqlalchemy
from sqlalchemy import Boolean, Column, DateTime, Date, Float, ForeignKey, Integer, JSON, PickleType, Text, Table, String
from sqlalchemy.orm import relationship
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
