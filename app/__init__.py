from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, ma, cors
from app.medico.routes import medico_api
from app.paciente.routes import paciente_api
from app.storages.routes import storage_api
from app.consulta.routes import consulta_api
from app.senhaesqueci.routes import senhaesqueci_api
from app.extensions import  mail as mail

#Iniciar app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    ma.init_app(app)
    cors.init_app(app,resources={r"/*":{"origins":"*"}})


    mail.init_app(app)



    app.register_blueprint(medico_api)
    app.register_blueprint(paciente_api)
    app.register_blueprint(storage_api)
    app.register_blueprint(consulta_api)
    app.register_blueprint(senhaesqueci_api)
    
    return app