from ..extensions import ma
from .model import Medico


class MedicoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Medico
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    nome=ma.String(required=True)
    cpf=ma.String(required=True)
    crm=ma.String(required=True)
    especialidade=ma.String(required=True)
    idade=ma.String(required=True)
    email=ma.Email(required=True)
    senha = ma.String(Load_only=True, required=True)