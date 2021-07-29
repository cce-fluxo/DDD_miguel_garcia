from app.extensions import db
from sqlalchemy.orm import backref

class Medico (db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    especialidade = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.Integer, nullable = False)
    crm = db.Column(db.Integer, nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    senha_hash = db.Column(db.String(100), nullable = False)

    


    def json(self):
        return {'nome': self.nome,
        'email':self.email,
        'cpf': self.cpf,
        'idade':self.idade,
        'especialidade':self.especialidade,
        'crm':self.crm,
        'idade':self.idade
        }