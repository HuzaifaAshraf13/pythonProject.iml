import os
from PyPDF2 import PdfMerger


def merge_pdfs(input_pdfs, output_pdf):
    merger = PdfMerger()

    for pdf in input_pdfs:
        merger.append(pdf)

    merger.write(output_pdf)
    merger.close()


if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")

    input_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  # Add your input PDF file names here
    output_file = os.path.join(desktop_path, "merged_output.pdf")  # Output file on the desktop

    input_files = [os.path.join(desktop_path, pdf) for pdf in input_files]  # Full paths to input files
    merge_pdfs(input_files, output_file)

    print(f"PDF files merged and saved as '{output_file}'.")
