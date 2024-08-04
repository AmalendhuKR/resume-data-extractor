import cv2
import numpy as np
from PIL import Image
import pytesseract

def preprocess_image(img):
     # Convert PIL image to OpenCV format (if needed)
    output_img = np.array(img)
    output_img = cv2.cvtColor(output_img, cv2.COLOR_RGB2BGR)
    
    # Grayscale conversion
    output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
    
    # Noise reduction with Gaussian Blur
    output_img = cv2.GaussianBlur(output_img, (5, 5), 0)
    
    # Thresholding to create binary image
    _, output_img = cv2.threshold(output_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Further noise reduction with dilation and erosion
    kernel = np.ones((3, 3), np.uint8)
    output_img = cv2.morphologyEx(output_img, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Ensure text is black and background is white
    output_img = cv2.bitwise_not(output_img)
    
    # Convert back to PIL image format
    output_img = Image.fromarray(output_img)
    
    return output_img


def extract_text_from_image(file_path):
    text = ""
    try:
        image = Image.open(file_path)
        preprocessed_image = preprocess_image(image)
        text = pytesseract.image_to_string(preprocessed_image, lang='eng', config='--psm 11')
        print("Extracting text from image")
    except Exception as e:
        print(f"Error reading image {file_path}: {e}")
    return text