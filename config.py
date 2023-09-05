import os, datetime


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ApplicationConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Stason2005@localhost:5432/postgres'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=120)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=1)
    ENDPOINT_MAKE_USER_OFFLINE_AFTER_N_SECONDS = 5

