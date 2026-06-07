from pathlib import Path

from ingestion.ingest_pdf import ingest_pdf


def ingest_folder(folder_path: str):

    folder = Path(folder_path)

    pdf_files = folder.glob("*.pdf")

    for pdf in pdf_files:

        print(f"\nProcessing: {pdf}")

        ingest_pdf(str(pdf))


if __name__ == "__main__":

    ingest_folder("data")
