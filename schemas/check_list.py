from ma import ma
from models.check_list import CheckListModel


class CheckListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CheckListModel
        load_instance = True
