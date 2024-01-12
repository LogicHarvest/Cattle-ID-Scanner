import os
from PIL import Image
import pytesseract
import openpyxl
import re

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Folder containing the images (assuming it's in the same directory as the script)
image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

# Excel file path
excel_file_path = 'output.xlsx'

# Create a new Excel workbook and add a sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = 'Image Filename'
sheet['B1'] = 'Original Text'
sheet['C1'] = 'Ear Tag Number'

# List to store results
results = []

# Process each image in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_folder, filename)

        try:
            # Load the image
            with Image.open(image_path) as image:
                # Pre-process the image
                image = image.resize((800, 600))  # Resize image
                image = image.convert('L')  # Convert to grayscale
                image = image.point(lambda p: p > 128 and 255)  # Thresholding

                # Apply OCR using Tesseract with custom configuration
                custom_config = r'--psm 6'
                ear_tag_number = pytesseract.image_to_string(image, config=custom_config)

                # Find numeric sequences using regular expression
                numeric_sequences = re.findall(r'\d+', ear_tag_number)

                # Concatenate numeric sequences found in consecutive lines
                ear_tag_number = ''.join(numeric_sequences)
                
                # Print debugging information
                print(f"Image: {filename}")
                print(f"Original Text: {ear_tag_number}")
                print(f"Numeric Sequences: {numeric_sequences}")
                print(f"Ear Tag Number: {ear_tag_number}")
                print("---")

                # Append the result to the list
                results.append((os.path.basename(image_path), ear_tag_number))


        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")

# Write results to Excel
for result in results:
    sheet.append(result)

# Save the Excel file
workbook.save(excel_file_path)

print(f"Processing complete. Results saved to {excel_file_path}")
