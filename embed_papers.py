import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Directory and file paths
paper_dir = "papers"
paper_files = ["papers_A.txt", "papers_B.txt"]

# Initialize list to store chunks
all_chunks = []

# Splitter config
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Loop over A and B files
for file_name in paper_files:
    file_path = os.path.join(paper_dir, file_name)
    with open(file_path, "r") as f:
        raw_text = f.read()

    if raw_text.strip():  # Skip empty files
        chunks = text_splitter.split_text(raw_text)
        all_chunks.extend(chunks)

print(f"✅ Prepared {len(all_chunks)} total chunks.")

# Embed and store
embeddings = OpenAIEmbeddings()
db = Chroma.from_texts(all_chunks, embeddings, persist_directory="chroma_db")
db.persist()
print("✅ Chroma DB created and saved to 'chroma_db/'")
