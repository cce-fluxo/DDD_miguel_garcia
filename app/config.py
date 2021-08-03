from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = "postgresql://omtdnjtkhisdsj:5389ace12b29e97db797ce9d2f4fb6ce5ea14b24965361050b0794885b24ec8a@ec2-34-194-14-176.compute-1.amazonaws.com:5432/d33glp2l0i2juu"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    JWT_SECRET_KEY = environ.get('SECRET_KEY')

    DEBUG = True
    