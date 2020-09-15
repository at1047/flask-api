from models import db, Todo, Attribute, links

def get_all(model):
    data = model.query.all()
    return data

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

def add_todo(name, attrs):
    instance = Todo(todo_name=name, status=False)
    db.session.add(instance)
    db.session.flush()
    commit_changes()
    return instance.todo_id

def get_one(model, id):
    data = model.query.filter_by(todo_id=id).all()[0]
    return data

def delete_todo(id):
    todo_obj = Todo.query.filter_by(todo_id=id).all()[0]
    db.session.delete(todo_obj)
    commit_changes()

def edit_todo(id, changes):
    instance = Todo.query.filter_by(todo_id=id).all()[0]
    for attr, new_value in changes.items():
        setattr(instance, attr, new_value)
    db.session.flush()
    commit_changes()

def commit_changes():
    db.session.commit()

def add_link(todo_id, attr_name):
    todo_obj = Todo.query.filter_by(todo_id=todo_id).all()[0]
    all_attr = get_all(Attribute)
    all_attr_id = [attr_name for attr in all_attr]
    if attr_name not in all_attr_id:
        add_instance(Attribute, attr_name=attr_name)
    attr_obj = Attribute.query.filter_by(attr_name=attr_name).all()[0]
    todo_obj.attr_link.append(attr_obj)
    commit_changes()

def del_link(todo_id, del_name):
    todo_obj = Todo.query.filter_by(todo_id=todo_id).all()[0]
    new_attr = [link.attr_name for link in todo_obj.attr_link if link.attr_name is not del_name]
    todo_name = todo_obj.todo_name
    todo_id = todo_obj.todo_id
    db.session.delete(todo_obj)
    instance = Todo(todo_id=todo_id, todo_name=todo_name)
    db.session.add(instance)
    # if link.attr_name is attr_name:
            # link.delete()
    # link_obj = links.query.filter_by(todo_id=todo_id, attr_id=attr_id).all()[0].delete
    # todo_obj.attr_link.clear() 
    commit_changes()

def get_link(todo_id):
    todo_obj = Todo.query.filter_by(todo_id=todo_id).all()[0]
    links = [link.attr_id for link in todo_obj.attr_link]
    attr = [Attribute.query.filter_by(attr_id=attr_id).all()[0].attr_name for attr_id in links]
    return attr
