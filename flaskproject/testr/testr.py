"""
Author: Leon Schuijtvlot
Studentno.: 14291584
This program is a webpage that can communicate with a webhook on github to
automaticly test a project.
"""

from flask import Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app

from werkzeug.utils import secure_filename

import os

bp = Blueprint('testr', __name__)



@bp.route('/testr')
def testr():
    "shows the webpage"
    return render_template('testr.html', files = [])

@bp.route('/testr', methods = ['POST'])
def upload():
    "this code allows for uploading, removing and downloading files from the server"

    # set the upload directory
    uploads_dir= request.form['project']
    UPLOAD_FOLDER = 'tests/' + uploads_dir
    current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)

    # make list of all the files in the folder to display on the webpage
    files = []
    for path in os.listdir(current_app.config['UPLOAD_FOLDER']):
        if os.path.isfile(os.path.join(current_app.config['UPLOAD_FOLDER'], path)):
            files.append(path)

    # if the upload/show button is clicked, upload the file and show the current files
    if request.method == 'POST' and request.form['action'] == "Upload/show files":
        ALLOWED_EXTENSIONS = {'py'}
        file = request.files['file']
        if file.filename != '' and allowed_file(file.filename, ALLOWED_EXTENSIONS):
           file = request.files['file']
           file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
           files.append(file.filename)

    # when the remove file button is clicked remove the specified file
    if request.method == 'POST' and request.form['action'] == "Remove file":
        file_name = request.form['rm_file']

        if file_name not in files:
            flash('File does not exit')
            return render_template('testr.html', files = files)

        os.system('rm ' + current_app.config['UPLOAD_FOLDER'] + '/' + file_name)
        files.remove(file_name)

    # when the download file button is clicked download the specified file
    if request.method == 'POST' and request.form['action'] == "Download file":
        file_name = request.form['rm_file']

        if file_name not in files:
            flash('File does not exit')
            return render_template('testr.html', files = files)

        return send_from_directory(app.config["UPLOAD_FOLDER"], file_name)

    return render_template('testr.html', files = files)






@bp.route('/webhook', methods=['POST'])
def consumetasks():
    "This function communicates with the webhook and runs the tests"

    if request.method == 'POST':

        file = request.json
        if file:

            # get the data from the webhook
            project_name = file['repository']['name']
            clone_url = file['repository']['clone_url']
            project_path = '/app/tests/' + project_name

            # get a list of all the the test files to copy them in the repository
            files = []

            for path in os.listdir(project_path):
                if os.path.isfile(os.path.join(project_path, path)):
                    files.append(path)

            cmd_files = ' '.join(files)

            # clone the project and run the tests in an virtual environment
            os.system('\
            cd ' + project_path +\
            ';git init\
            ;git clone ' + clone_url +\
            ';cp ' + cmd_files + ' ' + project_name +\
            '/;cd ' + project_name +\
            ';python3 -m venv venv\
            ;. venv/bin/activate\
            ;pip install -r requirements.txt\
            ;pytest --result-log=results.txt\
            ;deactivate'\
            )

            # open the results file to return the test results to the webhook
            with open(project_path + '/'+project_name+ '/results.txt') as f:
               results = f.read()

            # remove the project
            os.system('rm -r ' + project_path + '/' + project_name)

            return results


def allowed_file(filename, ALLOWED_EXTENSIONS):
    "This code checks if the file has the right extension"

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
