from datetime import datetime
from sqlalchemy import func
from flask import request
from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required
from api.responses import api_abort, api_response
from db.models import Post, User, db, Like, Dislike


class CreatePostResource(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()

        user = User.query.get(current_user.id)
        if not user:
            return api_abort(404, 'User not found')
        user.update_last_request_time()
        title = data.get('title')
        description = data.get('description')

        if not any([title, description]):
            return api_abort(403, "Provide all fields")

        new_post = Post(user_id=user.id, title=title, description=description)
        new_post.insert()
        return api_response(new_post.get_all(), "Post created")


class PostLikeResource(Resource):
    @jwt_required()
    def post(self, post_id):
        post = Post.query.get(post_id)

        if not post:
            return api_abort(404, 'Post not found')

        user_id = current_user.id
        user = User.query.get(user_id)

        existing_like = Like.query.filter_by(post_id=post_id, user_id=user_id).first()

        if existing_like:
            return api_abort(400, 'You already liked this post')

        like = Like(post_id=post_id, user_id=user_id)
        db.session.add(like)
        like.set_like_date()
        user.update_last_request_time()
        db.session.commit()

        return api_response(post.get_all(), "You Liked it!")


class PostDislikeResource(Resource):
    @jwt_required()
    def post(self, post_id):
        post = Post.query.get(post_id)

        if not post:
            return api_abort(404, 'Post not found')

        user_id = current_user.id
        user = User.query.get(user_id)

        existing_dislike = Dislike.query.filter_by(post_id=post_id, user_id=user_id).first()

        if existing_dislike:
            return api_abort(400, 'You already dislike this post')

        dislike = Dislike(post_id=post_id, user_id=user_id)
        db.session.add(dislike)
        dislike.set_dislike_date()
        user.update_last_request_time()
        db.session.commit()

        return api_response(post.get_all(), "You Disliked it!")


class AnalyticsResource(Resource):
    @jwt_required()
    def get(self, post_id):
        date_from_str = request.args.get('date_from')
        date_to_str = request.args.get('date_to')
        user = User.query.get(current_user.id)
        user.update_last_request_time()
        try:
            date_from = datetime.strptime(date_from_str, '%Y-%m-%d')
            date_to = datetime.strptime(date_to_str, '%Y-%m-%d')
        except ValueError:
            return {"error": "Invalid date format. Please use YYYY-MM-DD format."}, 400

        post = Post.query.get(post_id)
        if not post:
            return api_abort(404, "Post not found")

        likes_count = db.session.query(func.count()).filter(
            Like.post_id == post_id,
            Like.like_date >= date_from,
            Like.like_date <= date_to
        ).scalar()

        return {"likes_count": likes_count}
