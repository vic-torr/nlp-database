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

UPLOAD_DIRECTORY = "/home/vektor/code/nlp-database/nlp_db/uploads/"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
    
ALLOWED_EXTENSIONS = {'txt'}
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

api.add_resource(NlpDb, '/upload')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return 


if __name__ == '__main__':
    app.run(debug=True)

