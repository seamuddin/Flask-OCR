import os

from pdf2image import convert_from_path
import pytesseract
import re

def convert_pdf_to_text(image_path):
    os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'
    images = convert_from_path(image_path, 300)

    extracted_text = ''
    first_iteration = False
    for page in images:
        if first_iteration:
            text = pytesseract.image_to_string(page, lang='eng+ben', config='--psm 6')
            extracted_text += text + '\n'  # Add a newline between pages if needed
        else:
            first_iteration = False
    print(extracted_text)
    return extracted_text


def get_dict_from_text(text_data):

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