from flask import jsonify
from marshmallow import ValidationError
from ma import ma
from db import db

from src.controllers.to_do import ToDo, ToDoList, ToDoByName
from src.server.instance import server
from marshmallow import ValidationError

api = server.api
app = server.app


@app.before_request
def create_tables():
    db.create_all()

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

api.add_resource(ToDo, '/to_do/<int:id>')
api.add_resource(ToDoList, '/to_do')
api.add_resource(ToDoByName, '/to_do/filter/<string:name>')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
