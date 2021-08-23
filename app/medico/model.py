from enum import unique
from app.extensions import db,jwt
from sqlalchemy.orm import backref
from app.models import BaseModel
import bcrypt
from flask_jwt_extended import create_access_token
from app import storage

class Medico (db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    especialidade = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.String(40), nullable = False)
    crm = db.Column(db.Integer, nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    senha_hash = db.Column(db.LargeBinary(128), nullable = False)
    avatar = db.Column(db.String(64), unique = True, default = None )
    

    
    @property
    def avatar_url(self):
        if self.avatar:
            return storage.get_url(self.avatar)
        return None

    @avatar_url.setter
    def avatar_url(self,name):
        if self.avatar:
            storage.delete_object(self.avatar)
        self.avatar = name


    @property
    def senha(self):
        raise AttributeError('password is not a readable attribute')

    @senha.setter
    def senha(self, senha) -> None:
        self.senha_hash = bcrypt.hashpw(
            senha.encode(), bcrypt.gensalt())

    def verify_senha(self, senha: str) -> bool:
        return bcrypt.checkpw(senha.encode(), self.senha_hash)

    def token(self) -> str:
        return create_access_token(
            identity=self.id)