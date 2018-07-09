from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, timedelta

# Resources
from Resources.UserResource import UserRegister
from Resources.test import Test

app = Flask(__name__)



app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)

app.config.from_pyfile('config.cfg')
app.secret_key = app.config.get('SECRET_KEY')


api = Api(app)
api.add_resource(Test, '/test')
api.add_resource(UserRegister, '/sign-up')


if __name__ == '__main__':
    from Auth.Security import  identity, authenticate
    jwt = JWT(app, authenticate, identity)
    app.run()
