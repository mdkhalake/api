from flask import Response, request
from database.models import User
from flask_restful import Resource
from flask_jwt_extended import create_access_token

class UserApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

    
class UpdateApi(Resource):
    
    def delete(self, id):
        User.objects.get(id=id).delete()
        return 'Deleted', 200

    def get(self, id):
        user = User.objects.get(id=id).to_json()
        return Response(user, mimetype="application/json", status=200)
    
    def put(self, id):
        body = request.get_json()
        User.objects.get(id=id).update(**body)
        
        return 'Updated', 200

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
               
        access_token = create_access_token(identity=str(user.id))
        return {'token': access_token}, 200