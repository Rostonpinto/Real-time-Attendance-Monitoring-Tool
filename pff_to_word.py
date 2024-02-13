import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from docx import Document


def convert_pdf_to_word():
    # Select PDF file
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if pdf_file_path:
        # Create Word document
        doc = Document()

        # Open the PDF file
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)

            # Convert each page of the PDF to text and add it to the Word document
            for page in pdf_reader.pages:
                text = page.extract_text()
                doc.add_paragraph(text)

        # Save the Word document
        word_file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
        if word_file_path:
            doc.save(word_file_path)
            status_label.config(text="Conversion complete!")
    else:
        status_label.config(text="No PDF file selected.")


# Create GUI window
window = tk.Tk()
window.title("PDF to Word Converter")

# Create a button to select the PDF file
select_button = tk.Button(window, text="Select PDF File", command=convert_pdf_to_word)
select_button.pack(pady=20)

# Create a label to display the status
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()



