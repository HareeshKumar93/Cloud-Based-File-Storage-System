from flask import Flask, request, redirect, url_for, render_template
import boto3
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['S3_BUCKET'] = 'my-file-storage-bucket-harsha'
s3 = boto3.client('s3')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, app.config['S3_BUCKET'], filename)
        return redirect(url_for('index'))
    return redirect(request.url)

@app.route('/files/<filename>')
def download_file(filename):
    file_url = s3.generate_presigned_url('get_object',
                                         Params={'Bucket': app.config['S3_BUCKET'], 'Key': filename},
                                         ExpiresIn=3600)
    return redirect(file_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

