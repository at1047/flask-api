from models import db, Todo, Attribute, links

def get_all(model):
    data = model.query.all()
    return data

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

def delete_todo(id):
    # links.delete().where(
        # links.c.todo_id == id
    # )
    
    todo_obj = Todo.query.filter_by(todo_id=id).all()[0]
    # [todo_obj.attr_link.remove(link) for link in todo_obj.attr_link]
    db.session.delete(todo_obj)
    commit_changes()

def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()

def commit_changes():
    db.session.commit()

def add_link(todo, attr):
    todo_obj = Todo.query.filter_by(todo_id=todo).all()[0]
    attr_obj = Attribute.query.filter_by(attr_id=attr).all()[0]
    todo_obj.attr_link.append(attr_obj)
    commit_changes()

def get_link(this_todo_id):
    todo_obj = Todo.query.filter_by(todo_id=this_todo_id).all()[0]
    links = [link.attr_id for link in todo_obj.attr_link]
    attr = [Attribute.query.filter_by(attr_id=this_attr_id).all()[0].attr_name for this_attr_id in links]
    return attr
