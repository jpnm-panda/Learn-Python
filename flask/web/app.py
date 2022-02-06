from re import U
from flask import Flask, render_template, request, make_response, jsonify, send_file
import redis
import os
import werkzeug
import tempfile


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

UPLOAD_DIR = os.getenv("UPLOAD_DIR_PATH")
print('UPLOAD_DIR={}'.format(UPLOAD_DIR))
if UPLOAD_DIR is None:
   UPLOAD_DIR = os.getcwd()
   print('UPLOAD_DIR={}'.format(UPLOAD_DIR))

@app.route('/')
def hello():
    return '''
         <html><body>
        flask file upload/download example<br>
        <a href="/upload">upload</a><br>
        <a href="/data/download">download</a><br>
        </body></html>
        '''       
