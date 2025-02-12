import os

import PyPDF2


def pdf_to_text(pdf_filename: str) -> None:
    """
    Extracts text from the given PDF file and writes it to a text file
    with the same name but a .txt extension.

    Args:
        pdf_filename (str): Path to the PDF file.
    """
    # Verify the file has a .pdf extension
    if not pdf_filename.lower().endswith(".pdf"):
        print("Error: The input file must be a PDF.")
        return

    extracted_text = ""

    try:
        # Open the PDF file in binary mode
        with open(pdf_filename, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Iterate through each page in the PDF and extract text
            for page_number, page in enumerate(pdf_reader.pages, start=1):
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text
                else:
                    print(f"Warning: No text found on page {page_number}.")
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return

    # Create the output text filename by replacing '.pdf' with '.txt'
    txt_filename = os.path.splitext(pdf_filename)[0] + ".txt"

    try:
        with open(txt_filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(extracted_text)
        print(f"Text extracted and saved to {txt_filename}")
    except Exception as e:
        print(f"Error writing to text file: {e}")


# Example usage from the command line
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py filename.pdf")
    else:
        pdf_to_text(sys.argv[1])
