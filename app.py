from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from user import UserRegister
from security import authenticate, identity
from item import Item, Items

app = Flask(__name__)
app.secret_key = 'hari'
api = Api(app)

# creates new end point i.e /auth
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

app.run(debug=True)
