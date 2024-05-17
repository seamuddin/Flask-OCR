import os
from pdf2image import convert_from_path
import pytesseract
import re
from main.models import Voter

def convert_pdf_to_text(image_path, union):
    os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'
    images = convert_from_path(image_path, 300)

    extracted_text = ''
    main_list = []
    first = True
    for page in images:
        if first:
            first = False
            continue
        else:
            text = pytesseract.image_to_string(page, lang='eng+ben', config='--psm 6')
            # extracted_text += text + '\n'  # Add a newline between pages if needed
            manipulated_dict = get_dict_from_text(text)
            print(manipulated_dict)
            count = 0
            for data in manipulated_dict.get('name'):
                temp_dict = {}
                if len(manipulated_dict.get('ocupation')) > count:
                    voter_no = manipulated_dict.get('voter_no')[count].replace('\n', '').replace('\r','').replace('\\n','')
                    result = Voter.query.filter_by(voter_no=voter_no).first()
                    if not result:
                        temp_dict['name'] = data.replace('\n', '').replace('\r','').replace('\\n','')
                        temp_dict['voter_no'] = manipulated_dict.get('voter_no')[count].replace('\n', '').replace('\r','').replace('\\n','') if len(manipulated_dict.get('ocupation')) > count else ''
                        temp_dict['ocupation'] = manipulated_dict.get('ocupation')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('\\','').replace('-','') if len(manipulated_dict.get('ocupation')) > count else ''
                        temp_dict['fathers_or_husband'] = manipulated_dict.get('father')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('\\','').replace('-','') if len(manipulated_dict.get('father')) > count else ''
                        temp_dict['mother'] = manipulated_dict.get('mother')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('\\','').replace('-','') if len(manipulated_dict.get('mother')) > count else ''
                        temp_dict['birth_date'] = manipulated_dict.get('dob')[count].replace('\n', '').replace('\r','').replace('\\n','') if len(manipulated_dict.get('dob')) > count else ''
                        temp_dict['election_area'] = manipulated_dict.get('address')[count].replace('\n', '').replace('\r','').replace('\\n','').replace('-', '').replace('\n','').replace("\\",'') if len(manipulated_dict.get('address')) > count else ''
                        temp_dict['union'] = union
                        temp_dict['si'] =  manipulated_dict.get('voter_no')[count].replace('\n', '').replace('\r','').replace('\\n','')
                        main_list.append(temp_dict)
                count += 1
        

        
    return main_list


def get_dict_from_text(text_data):
    text_data = text_data.replace('এলাকার নাম :', '').replace('এলাকার নাম', '').replace('এলাকারনাম', '')
    name_pattern = r"নাম: (.*?)(?=\n|ভোটার নং:|\nভোটার নং:|\n\nভোটার নং|\s[০১২৩৪৫৬৭৮৯]|[০১২৩৪৫৬৭৮৯]|[০১২৩৪৫৬৭৮৯].|YOR.|FAY|[0123456789]|[0123456789].$)"
    voter_no_pattern = r"(?:ভোটার নং:|\sভোটার নং:) (.*?)(?=\n|ভোটার নং:|\nভোটার নং:|\n\nভোটার নং|পিতা:|$)"
    ocupation_pattern = r"পেশা: (.*?)(?=,|,জন্ম তারিখ:|\nজন্ম তারিখ:|\n\nজন্ম তারিখ:|$)"
    fathers_pattern = r"পিতা: (.*?)(?=\n|পিতা:|মাতা:|\nমাতা:|\n\nমাতা:|[০১২৩৪৫৬৭৮৯]$)"
    mothers_pattern = r"মাতা: (.*?)(?=\-\n|মাতা:|\sভোটার নং:|\n|\nভোটার নং:|\n\nভোটার নং:|\s[০১২৩৪৫৬৭৮৯]|[০১২৩৪৫৬৭৮৯]|[A-Z]|[a-z]|[8]|$)"
    dob_pattern = r"(?:জন্ম তারিখ:|,জন্ম তারিখ:|\n\nজন্ম তারিখ)(.*?)(?=\n|মাতা:|পেশা:|ঠিকানা:|মাইগ্রেট|কর্তন|তারিখ:|তারিখ্\u200c|\sভোটার নং:|\n$)"
    address_pattern = r"(?:ঠিকানা:|ঠিকানা)(.*?)(?=\n|\|\||\||\sভোটার নং:|\n|\nভোটার নং:|\n\nভোটার নং:|\s[০১২৩৪৫৬৭৮৯]|[০১২৩৪৫৬৭৮৯]|[A-Z]|[a-z]|[8]|$)"
    # Find all matches
    matches1 = re.findall(name_pattern, text_data)
    matches2 = re.findall(voter_no_pattern, text_data)
    matches3 = re.findall(ocupation_pattern, text_data)
    matches4= re.findall(fathers_pattern, text_data)
    matches5 = re.findall(mothers_pattern, text_data)
    matches6 = re.findall(dob_pattern, text_data)
    matches7 = re.findall(address_pattern, text_data)
    data = {
        'name' : matches1,
        'voter_no': matches2,
        'ocupation': matches3,
        'father' : matches4,
        'mother': matches5,
        'dob': matches6,
        'address': matches7
    }
    return data