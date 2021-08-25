from app.extensions import ma
from app.consulta.models  import Consulta
class ConsultaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Consulta
        load_instance = True
        ordered = True
    paciente_id = ma.Integer(load_only = True,required=True)
    medico_id = ma.Integer(load_only = True,required=True)
    id = ma.Integer(dump_only=True)
    hora = ma.String(required=False)
    data = ma.String(required=True)
    
    paciente = ma.Nested("PacienteSchema",many=False, only = ["nome","email"])
    medico = ma.Nested("MedicoSchema",many=False, only = ["nome","email"])