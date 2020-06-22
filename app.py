import json
from flask import request
from __init__ import create_app
import database
from models import Cats, Rooms, Staffs, Bookings, Locations, Owner, User
from datetime import datetime
import logging
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
log = logging.getLogger()

app = create_app()
app.config['SECRET_KEY'] = 'thisissecret'


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/createUser', methods = ['POST'])
def createUser():
    data = request.get_json()
    name = data['name']

    database.add_instance(User, name=name)
    return json.dumps("Added"), 200

@app.route('/getUsers')
def getUsers():
    users = database.get_all(User)
    all_users = []
    for u in users:
        newName = {
            "id": u.id,
            "name": u.name
        }
        all_users.append(newName)
    return json.dumps(all_users), 200

@app.route('/login/<name>')
def login(name):
    user = User.query.filter_by(name=name).first()
    login_user(user)
    return 'You are now logged in'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out'

@app.route('/home')
@login_required
def home():
    return 'The current user is ' + current_user.name

@app.route('/', methods=['GET'])
def fetch():
    cats = database.get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed,
            "ownerId": cat.ownerId
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200

@app.route('/listRoom', methods=['GET'])
def listRoom():
    rooms = database.get_all(Rooms)
    all_rooms = []
    for room in rooms:
        new_room = {
            "id": room.id,
            "name": room.name,
            "location": room.location
        }

        all_rooms.append(new_room)
    return json.dumps(all_rooms), 200

@app.route('/listLocation', methods=['GET'])
def listLocation():
    locations = database.get_all(Locations)
    all_locations = []
    for location in locations:
        new_location = {
            "id": location.id,
            "name": location.name,
        }

        all_locations.append(new_location)
    return json.dumps(all_locations), 200

#curl -XPOST -H "Content-type: application/json" -d \
#'{"name": "catty mcCatFace", "price": 5000, "breed": "bengal"}' \
#'127.0.0.1:5000/add'
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']
    ownerName = data['ownerName']
    ownerId = database.get_id(Owner, name=ownerName)

    log.info(ownerName)

    database.add_instance(Cats, name=name, price=price, breed=breed, ownerId=ownerId)
    return json.dumps("Added"), 200

@app.route('/test', methods=['POST'])
def test():
    # database.add_instance(Locations, name="STP")

    database.add_instance(Rooms, name="Townhall", locationID=database.get_id(Locations, name="STP"))


    #tmp = database.get_name(Rooms, id="1b703d34-8779-4a11-a03e-3c16e59008d8")
    #tmp = database.get_id(Rooms, id="1b703d34-8779-4a11-a03e-3c16e59008d8")
    # database.add_instance(Staffs, name="hermanchan", email="hkcph@msn.com")
    # staffid=database.get_id(Staffs, name="hermanchan")
    # roomid=database.get_id(Rooms, name="Curie")
    # starttime='2016-06-22 23:31:00'
    # endtime='2016-06-22 23:39:00'
    # #st = pytz.timezone('Asia/Hong_Kong').localize(datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S'))
    # #en = pytz.timezone('Asia/Hong_Kong').localize(datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S'))
    # #tmp=datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
    # #eventdate=tmp.strftime('%Y-%m-%d')
    # eventdate=datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    # tmp=database.check_availability_room_bookings(roomID=roomid, starttime=starttime, endtime=endtime, eventdate=eventdate)
    # #log.info(tmp)
    #database.add_instance(Bookings, staffID=staffid, roomID=roomid, starttime=starttime, endtime=endtime, eventdate=eventdate)
    return json.dumps(str("tmp")), 200

@app.route('/addRoom', methods=['POST'])
def addRoom():
    data = request.get_json()
    name = data['name']
    location = data['location']

    database.add_instance(Rooms, name=name, location=location)
    return json.dumps("Added"), 200

@app.route('/addLocation', methods=['POST'])
def addLocation():
    data = request.get_json()
    name = data['name']

    database.add_instance(Locations, name=name)
    return json.dumps("Added"), 200

@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200

@app.route('/deleteRoom/<room_id>', methods=['DELETE'])
def deleteRoom(room_id):
    database.delete_instance(Rooms, id=room_id)
    return json.dumps("Deleted"), 200

@app.route('/deleteLocation/<location_id>', methods=['DELETE'])
def deleteLocation(location_id):
    database.delete_instance(Locations, id=location_id)
    return json.dumps("Deleted"), 200

@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200

@app.route('/editRoom/<room_id>', methods=['PATCH'])
def editRoom(room_id):
    data = request.get_json()
    new_location = data['location']
    database.edit_instance(Cats, id=room_id, location=new_location)
    return json.dumps("Edited"), 200

@app.route('/getRoomBookings/<room_id>', methods=['GET'])
def getRoomBookings(room_id):
    bookings = database.get_room_bookings(room_id)
    all_bookings = []
    for booking in bookings:
        new_booking = {
            "id": booking.id,
            "starttime": str(booking.starttime),
            "endtime": str(booking.endtime)
        }

        all_bookings.append(new_booking)
    return json.dumps(all_bookings), 200

@app.route('/addOwner', methods=['POST'])
def addOwner():
    data = request.get_json()
    name = data['name']

    database.add_instance(Owner, name=name)
    return json.dumps("Added"), 200

# @app.route('/addLocation', methods=['POST'])
# def addLocation():
#     data = request.get_json()
#     name = data['name']
#
#     database.add_instance(Locations, name=name)
#     return json.dumps("Added"), 200

# import config
# from models import db

# import json, os
# #from .models import db
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# class Room:
#   def __init__(self, id, name, location):
#     self.id = id
#     self.name = name
#     self.location = location
#   def getName(self):
#     print("Hello my name is " + self.name)

# class Staff:
#   def __init__(self, id, name, email):
#     self.id = id
#     self.name = name
#     self.email = email
#   def getName(self):
#     print("Hello my name is " + self.name)

# class Booking:
#   def __init__(self, id, staff, room, starttime, endtime):
#     self.id = id
#     self.staff = staff
#     self.room = room
#     self.starttime = starttime
#     self.endtime = endtime
#   def getID(self):
#     print("Hello my name is " + str(self.id))

# p1 = Booking("id", "staff", "room", "11", "12")
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian",
#         "test": p1.id
#     }
# }

# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian",
#         "test": config.port
#     }
# }


# @app.route('/')
# def index():
#     headers = request.headers
#     return jsonify({"message": data}), 200
# #    auth = headers.get("X-Api-Key")
# #    if auth == 'asoidewfoef':
# #        return jsonify({"message": "OK: Authorized"}), 200
# #    else:
# #        return jsonify({"message": "ERROR: Unauthorized"}), 401
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
