from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import uuid

app = Flask('__name__', template_folder='templates')

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        
        # If we want to get a data from Form data then we need to use request.form 
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'asish' and password == '12345':
            return 'Success'
        return 'Failure'

# Upload a file in flask
@app.route('/file_upload', methods= ['POST'])
def file_upload():
    file = request.files.get('file')
    if file:
        return file.filename
    return 'no file submitted'

UPLOAD_FOLDER = 'downloads'

@app.route('/download_file', methods = ['POST'])
def download_file():
    file = request.files.get('file')
    print(str(os.path))
    project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the current Python script
    upload_dir = os.path.join(project_dir, UPLOAD_FOLDER)     # Construct the path to the upload folder

    # Ensure the upload directory exists, if not create it
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # Create unique file name for each files
    filename = f'{uuid.uuid4()}' + file.filename

    # Save the file to the upload directory
    file_path = os.path.join(upload_dir, filename)
    file.save(file_path)
    return render_template('download.html', filename = filename)

# Get file from the directory
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename)
    
@app.route('/handle_post', methods = ['POST'])
def handle_post():
    greeting = request.json['name']
    name = request.json['name']

    with open('downloads/file.txt', 'w') as f:
        f.write(f"{greeting}, {name}")
    
    return jsonify({'message': 'Successfully written'})

if __name__ == "__main__":
    app.run(debug= True, host='0.0.0.0')