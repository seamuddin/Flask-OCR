from flask import Blueprint, jsonify,Flask, render_template, request
from main.utils import convert_pdf_to_text
import tempfile
import os

route = Blueprint('bscic_api_service', __name__)


@route.route("/", methods=["GET"])
def get_token_route():
    return render_template("test.html")

@route.route("/upload", methods=["POST","GET"])
def uplaod_pdf():
    if request.method == 'POST':
        file = request.files['pdf']

        if 'pdf' not in request.files:
            return jsonify({'error': 'No PDF file provided'}), 400
        
        pdf_file = request.files['pdf']
        pdf_bytes = pdf_file.read()

        if not pdf_bytes:
            return jsonify({'error': 'PDF file is empty'}), 400
        else:

            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                pdf_file.save(tmp_file.name)
                text = convert_pdf_to_text(tmp_file.name)
            os.unlink(tmp_file.name)
            return jsonify({'data': text}), 200
            
            

    return render_template("test.html")


        

            
    