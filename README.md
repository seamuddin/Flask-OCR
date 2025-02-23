# Flask OCR Application

## About
This Flask-based OCR (Optical Character Recognition) application is specifically designed to extract text from PDF files, with special support for Bengali (Bangla) text. The project was developed to address the challenges of parsing Bengali text from PDF documents, providing a simple and efficient solution for text extraction.

## Features
- PDF to text conversion
- Specialized support for Bengali (Bangla) text recognition
- Simple web interface for file upload
- Plain text output format
- Easy-to-use REST API endpoints
- Support for multiple page PDFs

## Prerequisites
- Python 3.x
- Flask
- Tesseract OCR engine
- PyTesseract
- PDF2Image
- Poppler

## Installation

1. Clone the repository:
```bash
git clone https://github.com/seamuddin/Flask-OCR.git
cd Flask-OCR
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Install Tesseract OCR:
- For Ubuntu/Debian:
  ```bash
  sudo apt-get install tesseract-ocr
  sudo apt-get install tesseract-ocr-ben  # For Bengali language support
  ```
- For Windows:
  - Download and install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
  - Add Tesseract to your system PATH

5. Install Poppler:
- For Ubuntu/Debian:
  ```bash
  sudo apt-get install poppler-utils
  ```
- For Windows:
  - Download and install from: http://blog.alivate.com.au/poppler-windows/
  - Add to system PATH

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Access the web interface:
- Open your browser and navigate to `http://localhost:5000`
- Upload your PDF file
- Wait for processing
- Download or view the extracted text

## API Endpoints

### PDF Text Extraction
```
POST /upload
Content-Type: multipart/form-data
```

Parameters:
- `file`: PDF file (required)

Response:
```json
{
    "status": "success",
    "text": "Extracted text content..."
}
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Tesseract OCR for providing the OCR engine
- Flask framework for the web application structure
- Special thanks to the Bengali OCR community for resources and support

## Author
Seam Uddin

## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.
