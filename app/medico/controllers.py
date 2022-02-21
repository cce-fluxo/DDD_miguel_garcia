from flask.wrappers import Request
from app.medico.model import Medico
from flask import request, jsonify, abort,make_response
from app.extensions import db
from flask.views import MethodView 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.medico.schema import MedicoSchema
from app.filters import filter
import bcrypt
from sqlalchemy import exc






class MedicosCreate (MethodView): 
    def get(self):
        schema = MedicoSchema(many = True)
        pagina = request.args.get('pag', 1, type=int)
        medico = Medico.query.paginate(page=pagina, per_page=10)
        return jsonify(schema.dump(medico.items)),200


    def post(self):
        dados = request.json 
        schema = MedicoSchema()
        medico = schema.load(dados)

        db.session.add(medico)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        







        return schema.dump(medico),200

class MedicosDetails(MethodView): #/medico/details/<int:id>
    decorators = [jwt_required()]
    def get(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400       
        schema = filter.getSchema(
            qs=request.args,schema_cls=MedicoSchema)
        
        medico = Medico.query.get_or_404(id)
        return schema.dump(medico),200

    def put(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400

        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json,instance=medico)

        db.session.add(medico)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(medico),200

    def patch(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json, instance=medico, partial = True)

        db.session.add(medico)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(medico),200



    def delete(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        medico= Medico.query.get_or_404(id)
        db.session.delete(medico)
        db.session.commit()
        return {}, 200

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






