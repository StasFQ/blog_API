from flask import Flask
from flask_alembic import Alembic
from flask_jwt_extended import JWTManager
from api.posts.posts_apis import init_post_apis
from api.users.users_apis import init_users_apis
from config import ApplicationConfig
from db.models import setup_db, User

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
jwt = JWTManager(app)
setup_db(app)
init_post_apis(app)
init_users_apis(app)
alembic = Alembic()
alembic.init_app(app)

@jwt.user_identity_loader
def jwt_payload_user_identity_lookup(user):
        return user

@jwt.user_lookup_loader
def jwt_payload_user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()


if __name__ == '__main__':
    app.run()
