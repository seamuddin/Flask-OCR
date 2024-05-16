from flask import Blueprint, jsonify,Flask, render_template, request
from main.utils import convert_pdf_to_text
import os
from main.utils import get_dict_from_text
from main import db
from main.models import Voter
import asyncio

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

        text = asyncio.run(convert_pdf_to_text(pdf_path))
        data = {
            'contextData' : text
        }
    
        return render_template("upload.html", data=data)

        # return jsonify({'data': text}), 200

    return render_template("test.html")

@route.route("/store", methods=["POST","GET"])
def store_data():
    if request.method == 'POST':
        text = request.form.get('textdata')
        union = request.form.get('union')
        manipulated_dict = get_dict_from_text(text)
        prepared_data = []
        try:
            count = 0

            for data in manipulated_dict.get('name'):
                temp_dict = {}
                if len(manipulated_dict.get('ocupation')) > count:
                    voter_no = manipulated_dict.get('voter_no')[count].replace('\n', '').replace('\r','').replace('\\n','')
                    result = Voter.query.filter_by(voter_no=voter_no).first()
                    if not result:
                        temp_dict['name'] = data.replace('\n', '').replace('\r','').replace('\\n','')
                        temp_dict['voter_no'] = manipulated_dict.get('voter_no')[count].replace('\n', '').replace('\r','').replace('\\n','')
                        temp_dict['ocupation'] = manipulated_dict.get('ocupation')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('\\','').replace('-','') if len(manipulated_dict.get('ocupation')) > count else ''
                        temp_dict['fathers_or_husband'] = manipulated_dict.get('father')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('\\','').replace('-','') if len(manipulated_dict.get('father')) > count else ''
                        temp_dict['mother'] = manipulated_dict.get('mother')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('\\','').replace('-','') if len(manipulated_dict.get('mother')) > count else ''
                        temp_dict['birth_date'] = manipulated_dict.get('dob')[count].replace('\n', '').replace('\r','').replace('\\n','') if len(manipulated_dict.get('dob')) > count else ''
                        temp_dict['election_area'] = manipulated_dict.get('address')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('-', '').replace('\n','').replace("\\",'') if len(manipulated_dict.get('address')) > count else ''
                        temp_dict['union'] = union
                        temp_dict['si'] =  manipulated_dict.get('voter_no')[count].replace('\n', '').replace('\r','').replace('\\n','')
                        prepared_data.append(temp_dict)
                count += 1
            
            db.session.bulk_insert_mappings(Voter, prepared_data)
            db.session.commit()
            return jsonify({'success': 'data inserted successfully', 'data': prepared_data}), 200
        except Exception as e:
            db.session.rollback()
            db.session.close()
            return jsonify({'error': 'can not store data'+str(e), 'data': prepared_data}), 400
        
    return render_template("upload.html", data='')



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




            
    