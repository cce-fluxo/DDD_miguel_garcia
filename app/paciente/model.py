from sqlalchemy.orm import backref
from app.extensions import db

class Paciente (db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.Integer, nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    senha_hash = db.Column(db.String, nullable = False)
    

    



    def json(self):
        return {'nome': self.nome,
        'email':self.email,
        'cpf': self.cpf,
        'idade':self.idade
        
        }