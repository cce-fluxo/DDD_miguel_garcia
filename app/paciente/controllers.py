from app.paciente.model import Paciente
from flask import request, jsonify
from app.extensions import db
from flask.views import MethodView 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

#import bcrypt



class PacientesCreate (MethodView): 
    def get(self):
        paciente=Paciente.query.all()
        return jsonify([paciente.json() for paciente in paciente]), 200


    def post(self):
        dados = request.json 
        nome = dados.get('nome')
        cpf = dados.get ('cpf')
        idade = dados.get ('idade')
        email = dados.get ('email')
        senha = dados.get ('senha')
     
        paciente = Paciente.query.filter_by(email = email).first()

        if paciente:
            return {'error':'email já cadastrado'}, 400

    

        if not isinstance (nome,str) or not isinstance (idade, int):
            return {'error':'tipo invalido'}, 400

        if not isinstance (cpf,int) or not isinstance (email, str):
            return {'error':'tipo invalido'}, 400

        

        #senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())


        paciente = Paciente(nome=nome, cpf=cpf, idade=idade, email=email, senha=senha)
        db.session.add (paciente)
        db.session.commit()

        return paciente.json(), 200

class PacientesDetails(MethodView): #/paciente/details/<int:id>
    decorators = [jwt_required()]
    def get(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400

        paciente = Paciente.query.get_or_404(id)
        
        return paciente.json(), 200

    def put(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        paciente=Paciente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome')
        email = dados.get ('email')
        cpf = dados.get ('cpf')
        idade = dados.get ('idade')
       

        paciente.nome = nome
        paciente.email = email
        paciente.cpf = cpf
        paciente.idade = idade


        db.session.commit()

        return paciente.json(), 200

    def patch(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400

        paciente = Paciente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome', paciente.nome)
        email = dados.get ('email', paciente.email)
        cpf = dados.get ('cpf', paciente.cpf)
        idade = dados.get ('idade', paciente.idade)
        

        paciente.nome = nome
        paciente.email = email
        paciente.cpf = cpf
        paciente.idade = idade

        db.session.commit()

        return paciente.json(), 200
    
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






