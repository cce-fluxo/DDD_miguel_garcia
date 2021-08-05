from app.medico.model import Medico
from flask import request, jsonify
from app.extensions import db
from flask.views import MethodView 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

import bcrypt



class MedicosCreate (MethodView): 
    def get(self):
        medico=Medico.query.all()
        return jsonify([medico.json() for medico in medico]), 200


    def post(self):
        dados = request.json 
        nome = dados.get('nome')
        cpf = dados.get ('cpf')
        idade = dados.get ('idade')
        email = dados.get ('email')
        senha = dados.get ('senha')
        especialidade = dados.get('especialidade')
        crm = dados.get('crm')

        medico = Medico.query.filter_by(email = email).first()

        if medico:
            return {'error':'email já cadastrado'}, 400

    

        if not isinstance (nome,str) or not isinstance (idade, int):
            return {'error':'tipo invalido'}, 400
        
        if not isinstance (cpf,int) or not isinstance (email, str):
            return {'error':'tipo invalido'}, 400

        senha_hash = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())


        medico = Medico(nome=nome, cpf=cpf, idade=idade, email=email, especialidade=especialidade, crm=crm, senha_hash=senha_hash)
        db.session.add (medico)
        db.session.commit()

        return medico.json(), 200

class MedicosDetails(MethodView): #/medico/details/<int:id>
    decorators = [jwt_required()]
    def get(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400

        medico = Medico.query.get_or_404(id)
        
        return medico.json(), 200

    def put(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        medico=Medico.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome')
        email = dados.get ('email')
        cpf = dados.get ('cpf')
        idade = dados.get ('idade')
       

        medico.nome = nome
        medico.email = email
        medico.cpf = cpf
        medico.idade = idade


        db.session.commit()

        return medico.json(), 200

    def patch(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400

        medico = Medico.query.get_or_404(id)
        medico = Medico.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome', medico.nome)
        email = dados.get ('email', medico.email)
        cpf = dados.get ('cpf', medico.cpf)
        idade = dados.get ('idade', medico.idade)
        

        medico.nome = nome
        medico.email = email
        medico.cpf = cpf
        medico.idade = idade

        db.session.commit()

        return medico.json(), 200
    
    def delete(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        medico= Medico.query.get_or_404(id)
        db.session.delete(medico)
        db.session.commit()
        return medico.json(), 200

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






