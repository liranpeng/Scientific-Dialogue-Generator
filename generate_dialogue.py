# generate_dialogue.py

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# Load abstracts from files
def load_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

papers_A = load_text("papers_A.txt")
papers_B = load_text("papers_B.txt")

# Step 1: Generate a question from A’s research
llm = ChatOpenAI(temperature=0.7)

question_prompt = f"""
You are simulating a scientific Q&A.

Based on the following body of research abstracts from scientist A, generate a thoughtful, research-based question that scientist A might ask another expert in the field.

These are the abstracts:
\"\"\"
{papers_A}
\"\"\"

Only output the question as if from scientist A:
"""

question_from_A = llm.invoke(question_prompt)
print("🤔 Question from Scientist A:\n", question_from_A)

# Step 2: Check if B’s papers can answer it

# Split and embed B’s abstracts
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.create_documents([papers_B])
embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(chunks, embedding=embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

result = qa_chain.invoke({"query": question_from_A.content})
print("\n🧠 Answer from Scientist B:\n", result["result"])

