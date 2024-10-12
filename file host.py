from flask import Flask, render_template, request, redirect, send_from_directory, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'Recent Files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files[]')

    for file in files:
        if file.filename != '':
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return 'Files successfully uploaded!'


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/file_list')
def file_list():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify(files)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
