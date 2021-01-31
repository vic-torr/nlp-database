"""
    https://flask-restful.readthedocs.io/en/latest/quickstart.html
    python api.py
"""

from flask import Flask, request, flash, redirect, url_for
from flask_restful import fields, marshal_with
from flask_restful import reqparse, abort, Api, Resource
import traceback
import os
import io
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

# process words from texts
class NlpDb(Resource):
    def get(self):
        return {'request':'return'},200

    def delete(self):
        return {'request':'return'},200

    def put(self):
        return {'request':'return'},200
        
    def post(self):
        try:
            
            args = self.parser.parse_args()
            return {'request':'ok'},201
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)
    
    def error_message(self, key, msg, status=400):
        return {"key":key, "msg":msg, "statis":status}

api.add_resource(NlpDb, '/post')


if __name__ == '__main__':
    app.run(debug=True)

