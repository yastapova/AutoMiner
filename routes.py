import os.path

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from script import app
from forms import UploadForm
from werkzeug.utils import secure_filename

from mining import process_file

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            support = form.support.data
            confidence = form.confidence.data
            f = form.transactions_file.data

            filename = secure_filename(f.filename)
            data = f.readlines()

            output_filename, decode_errs = process_file(data, filename, support, confidence)

            file_exists = os.path.isfile(os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename))
            print("File %s exists: %s\n" % (output_filename, file_exists))
            
            if not file_exists:
                return render_template('/error.html', form=form, errmsg="nofile")

            return render_template('/results.html', form=form, result=output_filename, decode_errs=decode_errs)

    return render_template('/index.html', form=form)

@app.route('/download/<filename>', methods=['POST'])
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], (filename), as_attachment=True)
