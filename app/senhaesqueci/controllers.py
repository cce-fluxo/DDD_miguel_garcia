from flask import request,render_template, jsonify, abort, make_response
from flask.views import MethodView
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended.utils import decode_token
from flask_mail import Message
from app.extensions import mail, db
from app.models import BaseModel
from app.senhaesqueci.schemas import EmailSchema,SenhaSchema
from app.medico.model import Medico
from app.paciente.model import Paciente
from sqlalchemy import exc


class SenhaMail(MethodView):#/send_mail/reset
    def post(self):
        schema = EmailSchema()
        dados = schema.load(request.json)
        user = Medico.query.filter_by(email=dados['email']).first()
        if user:
            token = create_access_token(identity=user.id,additional_claims={'user_type' : "medico"})
            refresh_token = create_refresh_token(identity=user.id, additional_claims={'user_type': "medico"})
        else:
            user = Paciente.query.filter_by(email=dados['email']).first()
            if user:
                token = create_access_token(identity=user.id,additional_claims={'user_type': "paciente"})
                refresh_token = create_refresh_token(identity=user.id, additional_claims={'user_type': "paciente"})
            else:
                return {"Error":"Esse email não está cadastrado cadastrado"}, 400
        msg = Message(sender = 'mpgarcia@poli.ufrj.br',
        recipients=[user.email],
        subject = 'Mudança de senha',
        html = render_template('recupera.html', nome = user.nome, link=token))
        mail.send(msg)
        return {"Resultado":"envio feito"},200

class SenhaNova(MethodView): #/reset/<token>
    def patch(self,token):
        schema = SenhaSchema()
        dados = schema.load(request.json)

        token = decode_token(token)
        
        if token['user_type']=="medico":
            user = Medico.query.filter_by(id = token["sub"]).first()
        elif token['user_type']=="paciente":
            user = Paciente.query.filter_by(id = token["sub"]).first()
        
        if not user: return {"Error":"Token Inválido ou expirado"},404
        user.senha = dados["senha"]
        db.session.add(user)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        msg = Message(sender = 'mpgarcia@poli.ufrj.br',
        recipients=[user.email],
        subject = 'Senha Alterada',
        html = render_template('altera.html', nome = user.nome))
        mail.send(msg)
        mail.send(msg)
        return {},200