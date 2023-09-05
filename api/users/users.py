from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from werkzeug.exceptions import Unauthorized

from api.responses import api_response, api_abort
from db.models import User


class UserRegistrationResource(Resource):
    def post(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return api_abort(400, 'User with this email already exist')

        new_user = User(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        new_user.insert()
        access_token = create_access_token(identity=new_user.id)
        response_data = {
            'message': 'User registration successful',
            'access_token': access_token
        }

        return api_response(result=response_data, status_code=201)


class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        db_user: User = User.query.filter_by(email=email).first()
        # User authorization
        if not db_user:
            raise Unauthorized
        if not db_user.verify_password(password):
            raise Unauthorized

        db_user.update_last_login_time()
        db_user.update_last_request_time()
        # Generate access and refresh token
        access_token = create_access_token(identity=db_user.id)
        refresh_token = create_refresh_token(identity=db_user.id)

        return api_response({
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Logged in successfully")


class GetUserActivityResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)

        if not user:
            return api_abort(404, "User not found")

        data = {
            "last_login_date": user.last_login_date.strftime('%Y-%m-%d %H:%M:%S'),
            "last_request_date": user.last_request_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        return api_response(data, "Got user activity data")
