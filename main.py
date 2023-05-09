from flask import jsonify, Flask, Blueprint
from marshmallow import ValidationError
from ma import ma
from db import db

from src.controllers.check_list import CheckList, CheckListList, check_list_ns
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

api.add_resource(CheckList, '/check_list/<int:id>')
api.add_resource(CheckListList, '/check_list')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
