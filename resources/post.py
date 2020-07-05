from flask import Response, request
from database.models import User , Post
from flask_restful import Resource

from flask_jwt_extended import jwt_required,get_jwt_identity

class PostApi(Resource):
    
    def get(self):
        posts = Post.objects().to_json()
        return Response(posts, mimetype="application/json", status=200)
    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        post = Post(**body, author=user)
        post.save()
        #user.update(push__post=post)
        user.save()
        id = post.id
        return {'id': str(id)}, 200


class UpdatePostApi(Resource):
    @jwt_required
    def delete(self, id):
        Post.objects.get(id=id).delete()
        return 'Deleted', 200
    @jwt_required
    def get(self, id):
        post = Post.objects.get(id=id).to_json()
        return Response(post, mimetype="application/json", status=200)
        
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        post =Post.objects.get(id=id, author=user_id)
        body = request.get_json()
        Post.objects.get(id=id).update(**body)
        return 'Updated', 200
