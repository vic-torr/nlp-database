"""
    https://flask-restful.readthedocs.io/en/latest/quickstart.html
    python api.py
    
#TODO apidoc

"""
from flask import (Flask, request, flash, redirect, url_for,
                   abort, jsonify, send_from_directory)
from flask_restful import reqparse, abort, Api, Resource,  fields, marshal_with
import traceback
import os
import sys
from vocapi import Vocabulary
import json


vocab = Vocabulary()

UPLOAD_DIRECTORY = "/home/vektor/code/nlp-database/vocapi/uploads/"

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
    """
    @api {post} /upload/<filename> send file and parse vocabularies
    @apiName api
    @apiGroup Upload

    @apiParam (file) {String} text to be parsed
    @apiSuccess {Dict} vocab list
    """
    def post(self,filename):
        """Upload a file."""
        with open(os.path.join(UPLOAD_DIRECTORY, filename), "w") as fp:
            fp.write(request.data.decode())
        vocab.add_doc(request.data.decode())
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
        return {"Vocabulary": to_list(vocab.get_vocab())}


api.add_resource(GetVocab, "/word_vocab")


class Get2Vocab(Resource):
    def get(self):
        return {"Vocabulary": vocab.get_two_gram_vocab()}


api.add_resource(Get2Vocab, "/2_gram_vocab")


class GetDocsVocab(Resource):
    def get(self):
        return {"Vocabulary": vocab.get_vocab()}
        


api.add_resource(GetDocsVocab, "/docs_words")


class GetDocs2GramVocab(Resource):
    def get(self):
        return {"Vocabulary": vocab.get_vocab()}


api.add_resource(GetDocs2GramVocab, "/docs_2_gram")



if __name__ == '__main__':

    if len(sys.argv) == 1:
        host_string = "0.0.0.0"
    else:
        host_string = sys.argv[1]

    #app.config.from_pyfile(SETTINGS_PATH)
    app.run(host=host_string, debug=True)