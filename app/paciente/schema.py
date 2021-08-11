from ..extensions import ma
from .model import Paciente

class PacienteSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Paciente
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    nome=ma.String(required=True)
    cpf=ma.String(required=True)
    idade=ma.String(required=True)
    email=ma.Email(required=True)
    senha = ma.String(Load_only=True, required=True)