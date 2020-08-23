import json
from flask import request
from __init__ import create_app
import database
from models import Todo, Attribute
from datetime import datetime

app = create_app()

@app.route('/createTodo', methods = ['POST'])
def createTodo():
    new_name = request.args.get('name')
    database.add_instance(Todo, todo_name=new_name)
    return json.dumps("Added"), 200

@app.route('/createLink', methods = ['POST'])
def createLink():
    todo_id = request.args.get('todo_id')
    attr_id = data['attr_id']
    database.add_link(todo_id, attr_id)
    return json.dumps("Link created"), 200

@app.route('/getLinks')
def getLinks():
    todo_id = request.args.get('todo_id')
    links = database.get_link(todo_id)
    return json.dumps(links)

@app.route('/getTodo')
def getTodo():
    todos = database.get_all(Todo)
    all_todos = []
    for t in todos:
        new_todo = {
            "todo_id": t.todo_id,
            "todo_name": t.todo_name
        }
        all_todos.append(new_todo)
    return json.dumps(all_todos), 200

@app.route('/deleteTodo', methods=['DELETE'])
def deleteTodo():
    target_id = request.args.get('todo_id')
    database.delete_todo(target_id)
    return json.dumps("Deleted"), 200

@app.route('/editTodo', methods=['PATCH'])
def editTodo():
    data = request.get_json()
    target_id = request.args.get('todo_id')
    new_name = request.args.get('todo_name')
    database.edit_instance(Todo, todo_id=target_id, todo_name=new_name)
    return json.dumps("Updated"), 200

@app.route('/createAttr', methods = ['POST'])
def createAttr():
    new_attr = request.args.get('name')
    
    database.add_instance(Attribute, attr_name=new_attr)
    return json.dumps("Added"), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
