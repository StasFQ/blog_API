from flask_restful import Api

from api.posts.posts import CreatePostResource, PostLikeResource, PostDislikeResource, AnalyticsLikeResource, \
    AnalyticsDislikeResource


def init_post_apis(app):
    api = Api(app)

    api.add_resource(CreatePostResource, "/api/posts/")
    api.add_resource(PostLikeResource, "/api/<int:post_id>/like")
    api.add_resource(PostDislikeResource, "/api/<int:post_id>/dislike")
    api.add_resource(AnalyticsLikeResource, "/api/post/<int:post_id>/like/analytics")
    api.add_resource(AnalyticsDislikeResource, "/api/post/<int:post_id>/dislike/analytics")
