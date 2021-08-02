from ..extensions import ma
from .model import Product


class MedicoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Product
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    description = ma.String(required=True)
    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)