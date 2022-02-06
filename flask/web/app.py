from crypt import methods
from fileinput import filename
from re import U, template
from flask import Flask, render_template, request, make_response, jsonify, send_file
import redis
import os
import werkzeug
import tempfile
import datetime


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

@app.route('/upload')
def upload():
    now = datetime.datetime.now()
    timeString =now.strftime('%Y-%m-%d %H:%M')
    templateData = {
        'title': 'HELLO!',
        'name': 'flask!',
        'time': timeString
        }
    return render_template('upload.html', **templateData)

@app.route('/data/upload', methods=['POST'])
def upload_multipart():

    if 'uploadFile' not in request.files:
        make_response(jsonify({'result':'uploadFile is required.'}))
    
    file = request.file['uploadFile']
    print('file={}'.format(file))
    fileName = file.filename
    if '' == fileName:
          make_response(jsonify({'result':'filename must not empty.'}))
    
    saveFileName = werkzeug.utils.secure_filename(fileName)
    print('saveFileName={}'.format(saveFileName))
    if (len(saveFileName) == 0):
        fd, tempPath = tempfile.mkstemp()
        print('tempPath={}'.format(tempPath))
        saveFileName = os.path.basename(tempPath)
        print('saveFileName={}'.format(saveFileName))
        os.close(fd)
    
    print('UPLOAD_DIR={}'.format(UPLOAD_DIR))
    file.save(os.path.join(UPLOAD_DIR, saveFileName))
    return make_response(jsonify({'result':'upload OK.'}))
