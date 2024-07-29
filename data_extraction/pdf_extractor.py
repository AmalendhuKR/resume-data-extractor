from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        total_pages = reader.get_num_pages()
        for page_number in range(total_pages):
            page = reader.get_page(page_number)
            text += page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)

    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return text