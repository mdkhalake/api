from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/blog'
}

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=False)