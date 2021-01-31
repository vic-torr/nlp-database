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
from .vocabulary import Vocabulary

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


    
class Upload(Resource):
    def post(self,filename):
        """Upload a file."""
        with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(request.data)
        vocab.add_doc(request.data)
        # Return 201 CREATED
        return "", 201

api.add_resource(Upload, "/upload/<filename>")

class Download(Resource):
    def get(self,path):
        """Download a file."""
        return send_from_directory(UPLOAD_DIRECTORY,
                                   path, as_attachment=True)


class GetVocab(Resource):
    def get(self):
        return vocab.get_vocab()


api.add_resource(GetVocab, "/word_vocab")


class Get2Vocab(Resource):
    def get(self):
        return vocab.get_two_gram_vocab()


api.add_resource(Get2Vocab, "/2_gram_vocab")


class GetDocsVocab(Resource):
    def get(self):
        return vocab.get_vocab()


api.add_resource(GetDocsVocab, "/docs_words")


class GetDocs2GramVocab(Resource):
    def get(self):
        return vocab.get_vocab()


api.add_resource(GetDocs2GramVocab, "/docs_2_gram")


if __name__ == '__main__':
    app.run(debug=True)
