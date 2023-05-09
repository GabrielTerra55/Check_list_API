from flask import request
from flask_restx import Resource, fields
from sqlalchemy import Enum

from models.check_list import CheckListModel
from schemas.check_list import CheckListSchema

from src.server.instance import server

check_list_ns = server.check_list_ns

ITEM_NOT_FOUND = 'Check List not found.'

check_list_schema = CheckListSchema()
check_list_list_schema = CheckListSchema(many=True)


class StatusEnum(Enum):
    FEITO = 'feito'
    FAZENDO = 'fazendo'
    NAO_INICIADO = 'não iniciado'

item = check_list_ns.model('CheckList', {
    'name': fields.String(description='Check List name'),
    'description': fields.String(description='Check List description'),
    'deadline': fields.DateTime(description='Check List deadline'),
    'status': fields.String(description='Status da tarefa', attribute='status', enum=['feito', 'fazendo', 'não iniciado'])
})


class CheckList(Resource):

    def get(self, id):
        check_list_data = CheckListModel.find_by_id(id)
        if check_list_data:
            return check_list_schema.dump(check_list_data)
        return {
            'message': ITEM_NOT_FOUND
        }, 404

    @check_list_ns.expect(item)
    def put(self, id):

        check_list_data = CheckListModel.find_by_id(id)
        check_list_json = request.get_json()

        check_list_data.name = check_list_json['name']
        check_list_data.description = check_list_json['description']
        check_list_data.deadline = check_list_json['deadline']
        check_list_data.status = check_list_json['status']

        check_list_data.save_to_db()

        return check_list_schema.dump(check_list_data), 200

    def delete(self, id):

        check_list_data = CheckListModel.find_by_id(id)
        if check_list_data:
            check_list_data.delete_from_db()
            return '', 204

        return {'message', ITEM_NOT_FOUND}


class CheckListList(Resource):

    @check_list_ns.doc('Get all the Items')
    def get(self):
        return check_list_list_schema.dump(CheckListModel.find_all()), 200

    @check_list_ns.expect(item)
    @check_list_ns.doc('Create an Item')
    def post(self):
        check_list_json = request.get_json()
        check_list_data = check_list_schema.load(check_list_json)

        check_list_data.save_to_db()

        return check_list_schema.dump(check_list_data), 200
