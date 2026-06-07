from pypdf import PdfReader


def load_pdf(pdf_path: str):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":

    content = load_pdf("data/system_design.pdf")

    print(content[:1000])
