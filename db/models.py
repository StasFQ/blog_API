from datetime import datetime
from threading import Timer
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text,
    DateTime,
    Boolean
)
from werkzeug.security import generate_password_hash, check_password_hash

from config import ApplicationConfig

db = SQLAlchemy()


def setup_db(app, restart=False):
    with app.app_context():
        db.app = app
        db.init_app(app)


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    email = Column(String(100), nullable=False, unique=True)
    _password = Column(String, nullable=False)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    registration_data = Column(DateTime, default=datetime.utcnow)
    last_login_date = Column(DateTime, default=datetime.utcnow)
    last_request_date = Column(DateTime, default=datetime.utcnow)

    @property
    def password(self):
        print("Password can not be read.")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password, method="sha256")

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update_last_request_time(self):
        self.last_request_date = datetime.utcnow()
        db.session.commit()

    def update_last_login_time(self):
        self.last_login_date = datetime.utcnow()
        db.session.commit()


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    description = Column(Text, nullable=False)
    title = Column(String(70), nullable=False)
    likes = relationship('Like', backref='post', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def add_like(self):
        like = Like(post_id=self.id)
        db.session.add(like)
        db.session.commit()

    def get_all(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
        }


class Like(db.Model):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), nullable=False)
    like_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def set_like_date(self):
        self.like_date = datetime.utcnow()


class Dislike(db.Model):
    __tablename__ = 'dislikes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), nullable=False)
    dislike_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def set_dislike_date(self):
        self.dislike_date = datetime.utcnow()
