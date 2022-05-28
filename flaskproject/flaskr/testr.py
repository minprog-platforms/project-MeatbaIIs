from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory, current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
# from flask import Flask
import json

import os
from flask_socketio import SocketIO

bp = Blueprint('testr', __name__)


@bp.route('/testr')
def testr():
    # if request.method=='submit':
    #     project_link = request.form['project']
    #     error = None
    #
    #     if not project_link:
    #         error = 'projectname is required'
    #
    #     if error is not None:
    #         flash(error)
    #
    #     #os.system('cmd /k "git clone '+ project_link)
    #     os.system('cmd /k "date"')
    #     return redirect(url_for('/testr'))
    #     #return render_template('testr.html')#redirect(url_for('testr'))
    # else:
    return render_template('testr.html')

@bp.route('/testr', methods = ['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        uploads_dir= request.form['project']
        UPLOAD_FOLDER = 'tests/' + uploads_dir
        current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
        file = request.files['file']
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        #return redirect(url_for('download_file', name=filename))
        return redirect(url_for('testr'))


@bp.route('/webhook', methods=['POST'])
def consumetasks():
    if request.method == 'POST':
        file = request.json
        if file:
           UPLOAD_FOLDER = ''
           current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
           full_name = file['repository']['full_name']
           project_name = file['repository']['name']
           clone_url = file['repository']['clone_url']
           os.system('cd tests/' + project_name)
           os.system('git init')
           os.system('pytest --result-log=results.txt')
    return 'niks'
# @bp.route('/uploader', methods = ['GET', 'upload'])
# def upload_file():
#     if request.method == 'upload':
#        f = request.files['file']
#        f.save(secure_filename(f.filename))
#        return render_template('testr.html')




# @bp.route('/testr', methods = ['submit'])
# def testr():
#     if request.method('submit'):
#         project_link = request.form['project']
#         error = None
#
#         if not project_link:
#             error = 'projectname is required'
#
#         if error is not None:
#             flash(error)
#
#         os.system('cmd /k "git clone '+ project_link)
