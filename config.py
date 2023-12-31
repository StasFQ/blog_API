import os
import datetime

DOCKER = False


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ApplicationConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:stas123@localhost:5432/postgres'

    if DOCKER:
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres123@db:5432/postgres'

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=120)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=1)
