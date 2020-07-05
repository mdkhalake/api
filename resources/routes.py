from .user import  UserApi, UpdateApi , LoginApi
from .post import  PostApi ,UpdatePostApi

def initialize_routes(api):
    api.add_resource(PostApi,'/api/post')
    api.add_resource(UpdatePostApi,'/api/post/<id>')

    api.add_resource(UserApi,'/api/user')
    api.add_resource(UpdateApi,'/api/user/<id>')
    api.add_resource(LoginApi, '/api/login')
    
    
    
    
