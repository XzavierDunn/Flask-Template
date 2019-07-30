from flask_restplus import Api
from flask import Blueprint

# Here to show how to bring in the controllers
#from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

# How to add the controller paths to the namespace
# api.add_namespace(user_ns, path='/user')
# api.add_namespace(auth_ns)
