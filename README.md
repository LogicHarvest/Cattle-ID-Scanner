# Cattle-ID-Scanner
## Cattle Ear-Tag Scanner
### To utilize the Cattle-ID-Scanner, follow these steps:
####
#### Install Python & Tesseract:
#### Ensure Python is installed on your system.
#### Download and install Tesseract OCR.
#### Link to the Tesseract executable in your Python script:
```pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'```
### Install Dependencies:
#### Run the following command to install the necessary dependencies from the requirements.txt file:

```pip install -r requirements.txt```

### Prepare Images:

#### Add images to the /images directory.

### Run the Scanner:

Execute the main.py script to initiate the Cattle-ID-Scanner.

Required Dependencies:

Tesseract (OCR tool)
Python
openpyxl (for working with Excel files)
Pillow (Python Imaging Library)
pytesseract==0.3.8 (Python wrapper for Tesseract OCR)
