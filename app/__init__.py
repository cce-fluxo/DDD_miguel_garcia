from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt
from app.medico.routes import medico_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    app.register_blueprint(medico_api)
    return app