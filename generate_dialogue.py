# generate_dialogue.py

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# === CONFIGURATION ===
# You can modify this to test different topics
topic = "cloud microphysics"  # <- Your desired focus

# === Load abstracts from files ===
def load_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

papers_A = load_text("papers_A.txt")
papers_B = load_text("papers_B.txt")

# === Step 1: Generate a question from A’s research on a specific topic ===
llm = ChatOpenAI(temperature=0.7)

question_prompt = f"""
You are simulating a scientific conversation between two researchers.

Given the following collection of research abstracts from Scientist A, generate a thoughtful, technically accurate question that Scientist A might ask another scientist. 
Focus the question specifically on this topic: "{topic}".

These are Scientist A's abstracts:
\"\"\"
{papers_A}
\"\"\"

Only output the question, phrased as if it is being asked directly by Scientist A.
"""

question_from_A = llm.invoke(question_prompt)
print("🤔 Question from Scientist A:\n", question_from_A.content)

# === Step 2: Build retriever from Scientist B's papers ===
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.create_documents([papers_B])
embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(chunks, embedding=embeddings)

# === Step 3: Let B try to answer the question ===
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

result = qa_chain.invoke({"query": question_from_A.content})
print("\n🧠 Answer from Scientist B:\n", result["result"])

# === Optional: Show sources used ===
print("\n📚 Sources used:")
for doc in result["source_documents"]:
    print("-", doc.metadata.get("source", "[abstract snippet]"))
