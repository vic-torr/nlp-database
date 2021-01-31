"""
    https://flask-restful.readthedocs.io/en/latest/quickstart.html
    python api.py
"""

from flask import (Flask, request, flash, redirect, url_for,
                     abort, jsonify, send_from_directory)
from flask_restful import reqparse, abort, Api, Resource,  fields, marshal_with
import traceback
import os
from werkzeug.utils import secure_filename
from . import Vocabulary
vocab = Vocabulary()

UPLOAD_DIRECTORY = "/home/vektor/code/nlp-database/nlp_db/uploads/"

UPLOAD_FOLDER = UPLOAD_DIRECTORY
ALLOWED_EXTENSIONS = {'txt'}
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')




# process words from texts


api.add_resource(Upload, '/upload')
        

   
class Upload(Resource):
    def post(self):
        """Upload a file."""
        try:
            if "/" in filename:
                # Return 400 BAD REQUEST
                abort(400, "no subdirectories allowed")
            with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
                fp.write(request.data)
            vocab.add_doc(request.data)
            # Return 201 CREATED
            return "", 201
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)

    def error_message(self, key, msg, status=400):
        return {"key": key, "msg": msg, "statis": status}
        
    def list_files():
        """Endpoint to list files on the server."""
        files = []
        for filename in os.listdir(UPLOAD_DIRECTORY):
            path = os.path.join(UPLOAD_DIRECTORY, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)
api.add_resource(Upload, '/upload')        
        
class Download(Resource):
    def get(self):
        """Download a file."""
        try:
            return send_from_directory(UPLOAD_DIRECTORY, 
                            path, as_attachment=True)
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)
class GetVocab(Resource):
    def get(self):
        try:
            return vocab.get_vocab()
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)            
api.add_resource(GetVocab, "/word_vocab")

class Get2Vocab(Resource):
    def get(self):
        try:
            return vocab.get_two_gram_vocab()
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)            
api.add_resource(Get2Vocab, "/2_gram_vocab") 

class GetDocsVocab(Resource):
    def get(self):
        try:
            return vocab.get_vocab()
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)            
api.add_resource(Get2Vocab, "/docs_words")


class GetDocs2GramVocab(Resource):
    def get(self):
        try:
            return vocab.get_vocab()
        except Exception as e:
            traceback.print_exc()
            return self.error_message('error', e.value)            
api.add_resource(Get2Vocab, "/docs_2_gram")            


if __name__ == '__main__':
    app.run(debug=True)
