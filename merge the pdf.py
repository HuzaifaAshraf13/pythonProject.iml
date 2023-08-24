import os
import PyPDF2

def merge_pdfs(input_files, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in input_files:
        with open(pdf_file, 'rb') as pdf:
            pdf_merger.append(pdf)

    desktop_path = os.path.expanduser("~/Desktop")
    output_path = os.path.join(desktop_path, output_file)

    with open(output_path, 'wb') as output:
        pdf_merger.write(output)

    print(f"Merged {len(input_files)} PDFs into {output_path}")

if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")

    input_files = [
        os.path.join(desktop_path, '10398897_challan (1).pdf'),
        os.path.join(desktop_path, '10420276_challan (1).pdf')
    ]
    output_file = "merged_output.pdf"

    merge_pdfs(input_files, output_file)
