from ..extensions import ma
from .model import Medico, Product


class MedicoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Medico
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    nome=ma.String(required=True)
    cpf=ma.String(required=True)
    data_de_nascimento=ma.String(required=True)
    email=ma.Email(required=True)
    senha = ma.String(Load_only=True, required=True)