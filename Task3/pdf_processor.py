import pdfplumber


def extract_pdf_text(file_path):

    try:
        with pdfplumber.open(file_path) as pdf:

            text = ""

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"


        print("PDF text extracted successfully.")
        print(text)

        return text


    except Exception as e:
        print("PDF processing error:", e)



if __name__ == "__main__":

    file_path = input("Enter PDF file path: ")

    extract_pdf_text(file_path)