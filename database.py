from models import db, Bookings
from datetime import datetime
from sqlalchemy import and_, or_

import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
log = logging.getLogger()

def get_all(model):
    data = model.query.all()
    return data

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()

def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs:
        setattr(instance, attr, new_value)
    commit_changes()

def commit_changes():
    db.session.commit()

def get_id(model, name):
    return model.query.filter_by(name=name).all()[0].id

def get_room_bookings(room_id):
    return Bookings.query.filter_by(roomID=room_id).all()

def check_availability_room_bookings(roomID, starttime, endtime, eventdate):
    #tmp=Bookings.query.filter_by(roomID=roomID,eventdate=datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')).all()
    #tmp=Bookings.query.filter_by(eventdate=datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')).all()
    #tmp=Bookings.query.filter(starttime>'2016-06-22 22:00:00',starttime<'2016-06-22 23:01:00').all()
    tmp=Bookings.query.filter(roomID==roomID,or_(and_(Bookings.starttime<starttime,Bookings.endtime>starttime),and_(Bookings.starttime<endtime,Bookings.endtime>endtime),and_(Bookings.starttime>starttime,Bookings.endtime<endtime))).count()
    # tmp=Bookings.query.filter(and_(Bookings.starttime<starttime,Bookings.endtime>starttime)).all()
    # log.info(tmp)
    # tmp=Bookings.query.filter(and_(Bookings.starttime<endtime,Bookings.endtime>endtime)).all()
    # log.info(tmp)
    # tmp=Bookings.query.filter(and_(Bookings.starttime>starttime,Bookings.endtime<endtime)).all()
    # log.info(tmp)
    log.info(tmp)
    return tmp
    #return Bookings.query.filter_by(roomID=roomID,eventdate=datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')).all()
    #return Bookings.query.filter_by(roomID=room_id).all()
    #accounts, = session.query(Account.accounts).filter_by(id=account_id).first()
    #accounts, followers = session.query(Account.accounts, Account.followers).filter_by(id=account_id).first()
