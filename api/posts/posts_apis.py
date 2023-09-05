from flask_restful import Api

from api.posts.posts import CreatePostResource, PostLikeResource, PostDislikeResource, AnalyticsResource


def init_post_apis(app):
    api = Api(app)

    api.add_resource(CreatePostResource, "/api/posts/")
    api.add_resource(PostLikeResource, "/api/<int:post_id>/like")
    api.add_resource(PostDislikeResource, "/api/<int:post_id>/dislike")
    api.add_resource(AnalyticsResource, "/api/post/<int:post_id>/analytics")
