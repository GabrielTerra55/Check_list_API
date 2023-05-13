from flask import Flask, Blueprint
from flask_restx import Api
from ma import ma
from db import db

from marshmallow import ValidationError


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint,
                       doc='/docs',
                       title='Sample To Do API'
                       )

        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.to_do_ns = self.to_do_ns()

    def to_do_ns(self):
        return self.api.namespace(name='To Do', description='To Do related operations', path='/')

    def run(self):
        self.app.run(
            debug=True,
            host='0.0.0.0',
            port=5000
            
        )


server = Server()
