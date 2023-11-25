import os
from PIL import Image
import pytesseract
import openpyxl

# Folder containing the images
image_folder = 'path/to/images'

# Excel file path
excel_file_path = 'output.xlsx'

# Create a new Excel workbook and add a sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = 'Image Filename'
sheet['B1'] = 'Ear Tag Number'

# Function to process each image
def process_image(image_path):
    try:
        # Load the image
        image = Image.open(image_path)

        # Apply OCR using Tesseract
        ear_tag_number = pytesseract.image_to_string(image)

        # Validate the extracted number (add your validation logic here)

        # Write to Excel
        sheet.append([os.path.basename(image_path), ear_tag_number])
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

# Process each image in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_folder, filename)
        process_image(image_path)

# Save the Excel file
workbook.save(excel_file_path)