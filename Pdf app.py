import os
import tkinter as tk
from tkinter import ttk, filedialog
from PyPDF2 import PdfMerger


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=10)
        self.style.configure("TLabel", padding=5, font=("Helvetica", 12))

        self.instructions_label = ttk.Label(root, text="Select two PDFs to merge:")
        self.instructions_label.pack(pady=10)

        self.pdf1_button = ttk.Button(root, text="Select PDF 1", command=self.select_pdf1)
        self.pdf1_button.pack()

        self.pdf2_button = ttk.Button(root, text="Select PDF 2", command=self.select_pdf2)
        self.pdf2_button.pack()

        self.merge_button = ttk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=10)

        self.output_label = ttk.Label(root, text="")
        self.output_label.pack()

        self.pdf1_path = ""
        self.pdf2_path = ""

    def select_pdf1(self):
        self.pdf1_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    def select_pdf2(self):
        self.pdf2_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    def merge_pdfs(self):
        if self.pdf1_path and self.pdf2_path:
            merger = PdfMerger()
            merger.append(self.pdf1_path)
            merger.append(self.pdf2_path)

            desktop_path = os.path.expanduser("~/Desktop")
            output_path = os.path.join(desktop_path, "merged.pdf")

            merger.write(output_path)
            merger.close()

            self.output_label.config(text="PDFs merged successfully!")
        else:
            self.output_label.config(text="Please select both PDFs.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
