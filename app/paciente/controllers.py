from flask.wrappers import Request
from app.paciente.model import Paciente
from flask import request, jsonify, abort, make_response
from app.extensions import db
from flask.views import MethodView 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.paciente.schema import PacienteSchema
from app.filters import filter
import bcrypt
from sqlalchemy import exc 



class PacientesCreate (MethodView): 
    def get(self):
        schema = PacienteSchema(many = True)
        return jsonify(schema.dump(Paciente.query.all())),200


    def post(self):
        dados = request.json 
        schema = PacienteSchema()
        paciente = schema.load(dados)

        db.session.add(paciente)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return  schema.dump(paciente),200

class PacientesDetails(MethodView): #/paciente/details/<int:id>
    decorators = [jwt_required()]
    def get(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        schema = filter.getSchema(
            qs=request.args,schema_cls=PacienteSchema)
        paciente = Paciente.query.get_or_404(id)
        
        return schema.dump(paciente), 200

    def put(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        paciente=Paciente.query.get_or_404(id)
        schema = PacienteSchema()
        paciente = schema.load(request.json,instance=paciente)

        db.session.add(paciente)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(paciente),200

    def patch(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        paciente=Paciente.query.get_or_404(id)
        schema = PacienteSchema()
        paciente = schema.load(request.json,instance=paciente, partial = True)

        db.session.add(paciente)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(paciente),200
    
    def delete(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        paciente= Paciente.query.get_or_404(id)
        db.session.delete(paciente)
        db.session.commit()
        return paciente.json(), 200

class PacienteLogin(MethodView):
    def post(self):
        dados = request.json 
        email = dados.get ('email')
        senha = dados.get ('senha')
        
        paciente = Paciente.query.filter_by(email = email).first()
        if (not paciente) or (not bcrypt.checkpw(senha.encode(), paciente.senha_hash)):
            return {'error':'Email ou senha inválida'}, 400
        
        token = create_access_token(identity = paciente.id)
        
        return {"token" : token}, 200






