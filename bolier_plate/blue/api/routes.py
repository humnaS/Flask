from flask import Blueprint,jsonify, request
from flask_restful import Api,Resource
import pandas as pd
from werkzeug.utils import secure_filename


import sys 
import os
import json


dirname = os.path.dirname(os.path.abspath(__file__))
dirname_list = dirname.split("\\")[:-1]
dirname = "\\".join(dirname_list)
print(dirname)
path = dirname + "\\api"
print(path)
sys.path.append(path)


mod = Blueprint('api',__name__)
api = Api(mod)
df = None



class hello(Resource):
    def get(self):
        retJson = {"status":200,"msg":"ok"}
        return jsonify(retJson)

api.add_resource(hello, "/hello")
