from flask import Blueprint,jsonify, request
from flask_restful import Api,Resource
import pandas as pd
from werkzeug.utils import secure_filename

mod = Blueprint('api',__name__)
api = Api(mod)
df = None



class hello(Resource):
    def get(self):
        retJson = {"status":200,"msg":"ok"}
        return jsonify(retJson)

api.add_resource(hello, "/hello")
