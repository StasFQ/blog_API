from flask_restful import Api

from api.users.users import UserRegistrationResource, LoginResource, GetUserActivityResource


def init_users_apis(app):
    api = Api(app)

    api.add_resource(UserRegistrationResource, '/api/register')
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(GetUserActivityResource, '/api/user/<int:user_id>/activity')
