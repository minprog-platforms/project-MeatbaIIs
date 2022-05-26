from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
# from flask import Flask

import os
bp = Blueprint('testr', __name__)


@bp.route('/testr', methods = ('GET', 'sumbit', 'upload'))
def testr():
    if request.method=='submit':
        project_link = request.form['project']
        error = None

        if not project_link:
            error = 'projectname is required'

        if error is not None:
            flash(error)

        #os.system('cmd /k "git clone '+ project_link)
        os.system('cmd /k "date"')
        #return render_template('testr.html')#redirect(url_for('testr'))
    elif request.method == 'upload':
       f = request.files['file']
       f.save(secure_filename(f.filename))
    else:
        return render_template('testr.html')

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
