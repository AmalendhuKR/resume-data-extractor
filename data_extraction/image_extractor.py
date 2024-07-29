from PIL import Image

import pytesseract

def extract_text_from_image(file_path):
    text = ""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
    except Exception as e:
        print(f"Error reading image {file_path}: {e}")
    return text