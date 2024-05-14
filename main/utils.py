import os

from pdf2image import convert_from_path
import pytesseract
import re

def convert_pdf_to_text(image_path):
    os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'
    images = convert_from_path(image_path, 300)

    extracted_text = ''
    for page in images:
        text = pytesseract.image_to_string(page, lang='eng+ben', config='--psm 6')
        extracted_text += text + '\n'  # Add a newline between pages if needed
    print(extracted_text)
    return extracted_text


def get_dict_from_string(data):
    # Define the regex pattern to capture names
    name_pattern = r". নাম:\s(.*?)(?=\sভোটার নং:|\nভোটার নং:|\n\nভোটার নং:|\s[০১২৩৪৫৬৭৮৯]|[০১২৩৪৫৬৭৮৯]|[A-Z]|[8]|$)"
    # name_pattern = r". নাম:\s(.*?)(?=\sভোটার নং:|\s[০১২৩৪৫৬৭৮৯]|[০১২৩৪৫৬৭৮৯]|[A-Z]|$)"
    voter_no_pattern = r"ভোটার নং: (.*?)\s"
    ocupation_pattern = r"পেশা: (.*?)(?=\s|,জন্ম|$)"
    father_pattern = r"পিতা: (.*?)(?=\sমাতা:|\n|পিতা:|[০১২৩৪৫৬৭৮৯]|$)"
    mother_pattern = r"মাতা: (.*?)(?=\sমাতা:|\n|পিতা:|[০১২৩৪৫৬৭৮৯]|$)"
    birth_pattern = r"জন্ম তারিখ:(.*?)(?=\sমাতা:|\n|পিতা:|[০১২৩৪৫৬৭৮৯]|$)"
    address = r"ঠিকানা:(.*?)(?=\sমাতা:|\n|পিতা:|ঠিকানা:|[০১২৩৪৫৬৭৮৯]|$)"

    # Find all matches
    matches1 = re.findall(name_pattern, data)
    matches2 = re.findall(voter_no_pattern, data)
    matches3 = re.findall(ocupation_pattern,data)
    matches4 = re.findall(father_pattern,data)
    matches5 = re.findall(mother_pattern,data)
    matches6 = re.findall(birth_pattern,data)
    matches7 = re.findall(address,data)

    data = {
        'name' : matches1,
        'voter_no' : matches2,
        'occupation' : matches3,
        'father' : matches4,
        'mother' : matches5,
        'dob' : matches6,
        'address' : matches7
    }

    return data