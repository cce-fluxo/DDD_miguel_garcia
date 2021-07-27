from app.extensions import db
from app.association import association_table

class Medico (db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.Integer, nullable = False)
    idade = db.Column(db.Integer, nullable = False)

    
    consultas = db.relationship ('Consulta', backref = 'medico')
    exames = db.relationship ('Exame', backref = 'medico')
    receitas = db.relationship ('Receita', backref = 'medico')

    pacientes = db.relationship ('Paciente', secondary=association_table, backref='medico')

