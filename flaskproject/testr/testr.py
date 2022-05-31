from flask import Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app

from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
# from flask import Flask
import json

import os
from flask_socketio import SocketIO

bp = Blueprint('testr', __name__)



@bp.route('/testr')
def testr():

    return render_template('testr.html', files = [])

@bp.route('/testr', methods = ['POST'])
def upload():
    uploads_dir= request.form['project']
    UPLOAD_FOLDER = 'tests/' + uploads_dir
    current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
    files = []
    for path in os.listdir(current_app.config['UPLOAD_FOLDER']):
        if os.path.isfile(os.path.join(current_app.config['UPLOAD_FOLDER'], path)):
            files.append(path)

    if request.method == 'POST' and request.form['action'] == "Upload/show files":
        ALLOWED_EXTENSIONS = {'py'}
        file = request.files['file']
        if file.filename != '' and allowed_file(file.filename, ALLOWED_EXTENSIONS):
           file = request.files['file']
           file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
           files.append(file.filename)


    if request.method == 'POST' and request.form['action'] == "Remove file":
        file_name = request.form['rm_file']
        if file_name not in files:
            flash('File does not exit')
            return render_template('testr.html', files = files)
        os.system('rm ' + current_app.config['UPLOAD_FOLDER'] + '/' + file_name)
        files.remove(file_name)

    if request.method == 'POST' and request.form['action'] == "Download file":
        file_name = request.form['rm_file']
        return send_from_directory(app.config["UPLOAD_FOLDER"], file_name)

    return render_template('testr.html', files = files)






@bp.route('/webhook', methods=['POST'])
def consumetasks():
    if request.method == 'POST':
        file = request.json
        if file:
           full_name = file['repository']['full_name']
           project_name = file['repository']['name']
           clone_url = file['repository']['clone_url']
           #current_dir = os.listdir(current_path)\
           project_path = '/app/tests/'+project_name
           files = []
           for path in os.listdir(project_path):
               if os.path.isfile(os.path.join(project_path, path)):
                   files.append(path)
           cmd_files = ' '.join(files)

           os.system('\
           cd ' + project_path +\
           ';git init\
           ;git clone ' + clone_url +\
           ';cp ' + cmd_files + ' ' + project_name +\
           '/;cd ' + project_name +\
           ';python3 -m venv venv\
           ;. venv/bin/activate\
           ;pytest --result-log=results.txt\
           ;deactivate'\
           )
           with open(project_path + '/'+project_name+ '/results.txt') as f:
               results = f.read()
           os.system('rm -r ' + project_path + '/' + project_name)
           return results


def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
