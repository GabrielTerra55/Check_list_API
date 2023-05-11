from db import db
from sqlalchemy import Enum


class CheckListModel(db.Model):
    __tablename__ = 'check_list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum("feito", "fazendo", "não iniciado"),
                       default="não iniciado", nullable=False)

    def __init__(self, name, description, deadline, status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status

    def __repr__(self):
        return f'CheckListModel(name={self.name}, description={self.description},deadline={self.deadline}, status={self.status})'

    def json(self):
        return {
            'name': self.name,
            'description': self.description,
            'deadline': self.deadline,
            'status': self.status
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_deadline(cls, deadline):
        return cls.query.filter_by(deadline=deadline).all()

    @classmethod
    def find_by_status(cls, status):
        return cls.query.filter_by(status=status).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
