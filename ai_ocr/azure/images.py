import fitz


def pdf_to_pages(file_name: str):
    # Open the PDF
    pdf_document = fitz.open(file_name)
    pdf_path = file_name.replace(file_name.split("\\")[-1], "")
    # Iterate over each page
    i = 0
    for page in pdf_document:
        pix = page.get_pixmap(dpi=300)
        output = f"{pdf_path}/page_{i}.png"
        pix.save(output)
        i += 1
