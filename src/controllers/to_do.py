from flask import request
from flask_restx import Resource, fields
from sqlalchemy import Enum
from datetime import datetime

from models.to_do import ToDoModel
from schemas.to_do import ToDoSchema
from src.server.instance import server

to_do_ns = server.to_do_ns

ITEM_NOT_FOUND = 'To Do not found.'

to_do_schema = ToDoSchema()
to_do_list_schema = ToDoSchema(many=True)

default = {"status": "não iniciado"}

class StatusEnum(Enum):
    FEITO = 'feito'
    FAZENDO = 'fazendo'
    NAO_INICIADO = 'não iniciado'

item = to_do_ns.model('To Do', {
    'name': fields.String(description='To Do name', example="Revisão do Carro"),
    'description': fields.String(description='To Do description', example="Levar o carro para a revisão do sistema de freio"),
    'deadline': fields.DateTime(description='To Do deadline', example="2024-05-12T15:03:34.901Z"),
    'status': fields.String(description='To Do Status', example="não iniciado", enum=['feito', 'fazendo', 'não iniciado'])
})


class ToDo(Resource):

    def get(self, id):
        to_do_data = ToDoModel.find_by_id(id=id)
        if to_do_data:
            return to_do_schema.dump(to_do_data)
        return {
            'message': ITEM_NOT_FOUND
        }, 404

    @to_do_ns.expect(item)
    def put(self, id):

        to_do_data = ToDoModel.find_by_id(id)
        to_do_json = request.get_json()

        to_do_data.name = to_do_json['name']
        to_do_data.description = to_do_json['description']
        to_do_data.deadline = datetime.strptime(to_do_json['deadline'], '%Y-%m-%dT%H:%M:%S.%fZ')
        to_do_data.status = to_do_json['status']

        to_do_data.save_to_db()

        return to_do_schema.dump(to_do_data), 200

    def delete(self, id):

        to_do_data = ToDoModel.find_by_id(id)
        if to_do_data:
            to_do_data.delete_from_db()
            return '', 204

        return {'message', ITEM_NOT_FOUND}


class ToDoList(Resource):

    @to_do_ns.doc('Get all the Items')
    def get(self):
        return to_do_list_schema.dump(ToDoModel.find_all()), 200

    @to_do_ns.expect(item)
    @to_do_ns.doc('Create an Item')
    def post(self):
        to_do_json = request.get_json()
        if not to_do_json['status']:
            to_do_json['status'] = default.get('status')
        to_do_data = to_do_schema.load(to_do_json)

        to_do_data.save_to_db()

        return to_do_schema.dump(to_do_data), 200

class ToDoByName(Resource):
    @to_do_ns.doc('Get iten by name')
    def get(self, name):
        to_do_data = ToDoModel.find_by_name(name=name)
        if to_do_data:
            return to_do_schema.dump(to_do_data)
        return {
            'message': ITEM_NOT_FOUND
        }, 404
    