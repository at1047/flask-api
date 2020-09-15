import json
from flask import request, Response
from __init__ import create_app
import database
from models import Todo, Attribute
from datetime import datetime
from flask_cors import CORS, cross_origin

app = create_app()

# Allow for CORS
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

@app.route('/todo', methods = ['POST'])
def create_todo():
    data = request.json
    try:
        id = database.add_todo(name=data['name'], attrs=None)
        resp = Response(json.dumps({
            "todo_id": id,
            "todo_name": data['name'],
            "todo_attr": [],
            "state": False
        }));
        status = 200
    except:
        resp = "duplicate name"
        status = 400
    return resp, status

@app.route('/todo', methods = ['GET'])
def get_todo():
    id = request.args.get('id', default = None)
    if id is None:
        todos = database.get_all(Todo)
        data = [{"todo_id": t.todo_id, "todo_name": t.todo_name, "todo_attr": [attr.attr_name for attr in t.attr_link], "status": t.status} for t in todos] 
        status = 200
    else:
        try:
            todos = database.get_one(Todo, id) 
            data = [{"todo_id": t.todo_id, "todo_name": t.todo_name, "todo_attr": [attr.attr_name for attr in t.attr_link], "status": t.status} for t in todos] 
            status = 200
        except:
            data = "does not exist"
            status = 400
    resp = Response(json.dumps(data))
    return resp, status

@app.route('/todo', methods=['DELETE'])
def delete_todo():
    id = request.args.get('id')
    try:
        database.delete_todo(id)
        status = 200
    except:
        status = 400
    return "deleted", status

@app.route('/todo', methods=['PATCH'])
def edit_todo():
    id = request.args.get('id')
    data = request.json
    changes = data["changes"]
    for attr, new_value in changes.items():
        database.edit_todo(id, { attr: new_value })
    instance = database.get_one(id)
    resp = Response(json.dumps({
        "todo_id": instance.todo_id,
        "todo_name": instance.todo_name,
        "todo_attr": [attr.attr_name for attr in instance.attr_link],
        "status": instance.status
    }))
    return resp, 200

# @app.route('/attribute', methods = ['POST'])
# def create_attribute():
    # data = request.json
    # id = database.add_instance(Attribute, attr_name=data['name'])
    # resp = Response(json.dumps({
        # "attr_id": id,
        # "attr_name": data['name'],
    # }))
    # return resp, 200

@app.route('/link', methods = ['POST'])
def create_link():
    data = request.json
    todo_id = data[ 'todo_id' ]
    attr_name = data[ 'attr_name' ]
    database.add_link(todo_id=todo_id, attr_name=attr_name)
    return json.dumps("Link created"), 200

@app.route('/link')
def get_todo_attribute():
    todo_id = request.args.get('todo')
    links = database.get_link(todo_id)
    return json.dumps(links)

@app.route('/link', methods = ['DELETE'])
def delete_link():
    todo_id = request.args.get('todo')
    attr_name = request.args.get('attr')
    database.del_link(todo_id, attr_name)    
    return "success", 200

@app.route('/attribute')
def get_all_attribute():
    attrs = database.get_all(Attribute)
    data = [{"attr_id": a.attr_id, "attr_name": a.attr_name} for a in attrs] 
    resp = Response(json.dumps(data))
    return resp, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
