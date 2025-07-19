import os #os is used to handle file paths and folders safely.
from flask import Flask, request, render_template, redirect, url_for
from parser import *

app = Flask(__name__) #creates flask app
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET']) # / means flask route Post-The browser sends the file data to the server.
def index(): #opening a page = GET request. even if it means home page .This is a function that runs when someone opens your website at /.
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        text = extract_text_from_pdf(file_path)
        parsed_data = {
            'name': extract_name(text),
            'email': extract_email(text),
            'phone': extract_phone(text),
            'skills': extract_skills(text),
            'education': extract_education(text),
            'raw_text': text
        }
        return render_template('index.html', parsed_data=parsed_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
