from app.extensions import db
from app.models import BaseModel


class Consulta (BaseModel):
    __tablename__='consulta'
    id = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.String,nullable = False)
    hora =  db.Column(db.String,nullable = False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))