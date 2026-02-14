from sqlalchemy import create_engine

class Config:
    SECRET_KEY = 'secret'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Junior021205$$$@127.0.0.1:3306/BDIDGS804'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
