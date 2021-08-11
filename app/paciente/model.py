from sqlalchemy.orm import backref
from app.extensions import db, jwt 
from app.models import BaseModel
import bcrypt
from flask_jwt_extended import create_access_token

class Paciente (db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.Integer, nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    senha_hash = db.Column(db.LargeBinary(128), nullable = False)
    

    



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