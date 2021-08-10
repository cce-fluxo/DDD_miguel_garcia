from app.extensions import db
from sqlalchemy import exc
from flask import abort,make_response,jsonify



class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def create(cls,**data)-> object:
        return cls(**data)
    
    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()
    
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()