import os
from flask import Flask, request, render_template
from parser import *

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            text = extract_text_from_pdf(file_path)

            data = {
                "Name": extract_name(text),
                "Email": extract_email(text),
                "Phone": extract_phone(text),
                "Skills": extract_skills(text),
                "Education": extract_education(text)
            }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
