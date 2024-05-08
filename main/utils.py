from pdf2image import convert_from_path
import pytesseract

def convert_pdf_to_text(image_path):
    images = convert_from_path(image_path, 250)

    extracted_text = ''
    for page in images:
        text = pytesseract.image_to_string(page, lang='eng+ben', config='--psm 6')
        extracted_text += text + '\n'  # Add a newline between pages if needed
    
    return extracted_text

