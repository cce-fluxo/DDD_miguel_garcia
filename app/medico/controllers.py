from flask.wrappers import Request
from app.medico.model import Medico
from flask import request, jsonify
from app.extensions import db
from flask.views import MethodView 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.medico.schema import MedicoSchema
from app.filters import filter
import bcrypt






class MedicosCreate (MethodView): 
    def get(self):
        schema = MedicoSchema(many = True)
        return jsonify(schema.dump(Medico.query.all())),200


    def post(self):
        dados = request.json 
        schema = MedicoSchema()
        medico = schema.load(dados)
        medico.save()
        return schema.dump(medico),200

class MedicosDetails(MethodView): #/medico/details/<int:id>
    decorators = [jwt_required()]
    def get(self, id):
        schema = filter.getSchema(
            qs=request.args,schema_cls=MedicoSchema)
        
        medico = Medico.query.get_or_404(id)
        return schema.dump(medico),200

    def put(self, id):


        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json,instance=medico)

        medico.save()
        return schema.dump(medico),200

    def patch(self, id):

        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json, instance=medico, partial = True)

        medico.save()
        return schema.dump(medico),200



    def delete(self, id):

        medico= Medico.query.get_or_404(id)
        medico.delete(medico)
        return {}, 204

class MedicoLogin(MethodView):
    def post(self):
        dados = request.json 
        email = dados.get ('email')
        senha = dados.get ('senha')
        
        medico = Medico.query.filter_by(email = email).first()
        if (not medico) or (not bcrypt.checkpw(senha.encode('utf8'), medico.senha_hash)):
            return {'error':'Email ou senha inválida'}, 400
        
        token = create_access_token(identity = medico.id)
        
        return {"token" : token}, 200






