from app.extensions import ma

class EmailSchema(ma.SQLAlchemySchema):
    email = ma.Email(required=True)

class SenhaSchema(ma.SQLAlchemySchema):
    senha = ma.String(required=True,load_only = True)