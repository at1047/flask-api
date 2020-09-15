import flask_sqlalchemy
from sqlalchemy import Boolean, Column, DateTime, Date, Float, ForeignKey, Integer, JSON, PickleType, Text, Table, String
from sqlalchemy.orm import relationship

db = flask_sqlalchemy.SQLAlchemy()

links = db.Table('links',
    db.Column('todo_id', db.Integer, db.ForeignKey('todo.todo_id')),
    db.Column('attr_id', db.Integer, db.ForeignKey('attribute.attr_id'))
)

class Todo(db.Model):
    todo_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    todo_name = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    attr_link = db.relationship('Attribute', secondary=links, backref=db.backref('todos', lazy='dynamic'))

class Attribute(db.Model):
    attr_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    attr_name = db.Column(db.String(20), nullable=False)
