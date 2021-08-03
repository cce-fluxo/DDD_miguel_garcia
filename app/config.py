from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #DATABASE_URI = 'postgresql://nxbmihmxeodwag:7eb0e748ccb1d4f4ea32f3cd5e1f7d9b853b3b09dae76f7d35a630358a28b3ba@ec2-44-194-112-166.compute-1.amazonaws.com:5432/d8u4vvf6i90jfn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    JWT_SECRET_KEY = environ.get('SECRET_KEY')

    DEBUG = True
    