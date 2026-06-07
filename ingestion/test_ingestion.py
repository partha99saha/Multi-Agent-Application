from pdf_loader import load_pdf
from chunker import create_chunks

text = load_pdf("data/system_design.pdf")

chunks = create_chunks(text)

print(f"\nChunks Created: {len(chunks)}\n")

for i, chunk in enumerate(chunks[:3]):

    print(f"\nChunk {i+1}")
    print("-" * 50)

    print(chunk[:300])
