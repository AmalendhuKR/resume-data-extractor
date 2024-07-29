import os

from config import INPUT_PATH_PDF, INPUT_PATH_IMAGE, OUTPUT_PATH

from data_extraction.pdf_extractor import extract_text_from_pdf
from data_extraction.image_extractor import extract_text_from_image

def process_resumes(folder_path):
    output_folder=OUTPUT_PATH+"/pdfs"
    os.makedirs(output_folder, exist_ok=True)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if file_path.endswith('.pdf'):
            file_content = extract_text_from_pdf(file_path)
        
        output_file_name = os.path.splitext(file_name)[0] + '.txt'
        output_file_path = os.path.join(output_folder, output_file_name)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(file_content)

        print("Successfully generated the result")

def main():
    process_resumes(INPUT_PATH_PDF)
    # print(extract_text_from_image(os.path.join(INPUT_PATH_IMAGE, "image_01.jpg")))

if __name__ == "__main__":
    main()