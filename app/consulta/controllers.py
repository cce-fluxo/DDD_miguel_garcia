from flask import request,jsonify
from flask.views import MethodView

from app.medico.model import Medico
from app.paciente.model import Paciente

from app.consulta.models import Consulta
from app.consulta.schemas import ConsultaSchema


class ConsultaGet(MethodView): #/paciente
    def get(self):

        schema = ConsultaSchema(many = True)
        return jsonify(schema.dump(Consulta.query.all())),200

class ConsultaPost(MethodView): #/paciente/create
    def post(self):
        
        dados = request.json
        schema = ConsultaSchema()
        medico = Medico.query.get_or_404(dados['medico_id'])
        paciente = Paciente.query.get_or_404(dados['paciente_id'])

        schema.paciente = paciente
        schema.medico= medico
        

        consulta = schema.load(dados)
        consulta.save()
        medico.consulta.append(consulta)
        paciente.consulta.append(consulta)
        return schema.dump(consulta),201