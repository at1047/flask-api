import json
from flask import request
from __init__ import create_app
import database
from models import Todo
from datetime import datetime

app = create_app()

@app.route('/createTodo', methods = ['POST'])
def createTodo():
    data = request.get_json()
    name = data['name']

    database.add_instance(Todo, name=name)
    return json.dumps("Added"), 200

@app.route('/getTodo')
def getTodo():
    todos = database.get_all(Todo)
    allTodos = []
    for t in todos:
        newTodo = {
            "id": t.id,
            "name": t.name
        }
        allTodos.append(newTodo)
    return json.dumps(allTodos), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
