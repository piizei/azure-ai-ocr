import fitz
import os


def pdf_to_pages(file_name: str):
    # Open the PDF
    pdf_document = fitz.open(file_name)
    pdf_path, _ = os.path.split(file_name)
    # Iterate over each page
    i = 0
    for page in pdf_document:
        pix = page.get_pixmap(dpi=300)
        output = os.path.join(pdf_path, f"page_{i}.png")
        pix.save(output)
        i += 1
