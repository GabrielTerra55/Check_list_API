from ma import ma
from models.to_do import ToDoModel


class ToDoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ToDoModel
        load_instance = True
