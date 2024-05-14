from flask import Blueprint, jsonify,Flask, render_template, request
from main.utils import convert_pdf_to_text
import tempfile
import os
from main.utils import get_dict_from_string
route = Blueprint('bscic_api_service', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}


@route.route("/", methods=["GET"])
def get_token_route():
    return render_template("test.html")

@route.route("/upload", methods=["POST","GET"])
def uplaod_pdf():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return jsonify({'error': 'No PDF file provided'}), 400

        pdf_file = request.files['pdf']

        if not allowed_file(pdf_file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
        pdf_file.save(pdf_path)

        # text = convert_pdf_to_text(pdf_path)
        text = 'hfsfsfjklsf hslkhfslfs'
        data = {
            'contextData' : text
        }
    
        return render_template("upload.html", data=data)

        # return jsonify({'data': text}), 200
    



    return render_template("test.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@route.route("/store", methods=["POST"])
def store_data():
    if request.method == 'POST':

        text = get_dict_from_string(request.form['textdata'])
        union = request.form['union']

        return jsonify({'error': 'Okay', 'data': text}), 200

        # return jsonify({'data': text}), 200
    



    return render_template("test.html")



            
    