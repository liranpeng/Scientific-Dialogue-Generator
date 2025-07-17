
# Scientific Dialogue Generator

This project generates simulated scientific conversations between two researchers, based on the abstracts of their published papers. It allows users to input two scientist names and then:

1. Searches Semantic Scholar for all papers authored by Scientist A and Scientist B.
2. Extracts and embeds the abstracts of their papers.
3. Automatically generates a research question that Scientist A might ask based on their research themes.
4. Simulates an answer from Scientist B grounded in their own publications.
5. Provides sources for the answer by referencing where in the abstracts the information comes from.

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Scientific-Dialogue-Generator.git
cd Scientific-Dialogue-Generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Ensure you also have [Chromadb](https://www.trychroma.com/) and `langchain`, `openai`, and `tiktoken` installed.

### 3. Set your OpenAI API key

```bash
export OPENAI_API_KEY=your-key-here
```

---

## 🚀 How to Use

### Step 1: Download papers

```bash
python get_papers.py
```

This will save abstracts for the two scientists in the `abstracts/` folder.

### Step 2: Embed abstracts

```bash
python embed_all.py
```

Chunks and stores vector embeddings in the `chroma_db/` folder.

### Step 3: Generate question and answer

```bash
python generate_dialogue.py
```

Generates a natural question and answer pair between Scientist A and Scientist B.

---

## 📁 Project Structure

```
Scientific-Dialogue-Generator/
├── abstracts/              # Stored abstracts from Semantic Scholar
├── chroma_db/              # Vector DB created by Chroma
├── get_papers.py           # Fetch abstracts
├── embed_all.py            # Create embeddings
├── generate_dialogue.py    # Generate Q&A dialogue
└── README.md
```

---

## 💡 Example

- **Scientist A:** Peter Blossey  
- **Scientist B:** Christopher Bretherton

**Generated Question from A:**  
> What are the main processes that control the isotopic composition of water vapor near the surface of tropical oceans, and how do changes in precipitation rate impact the isotopic depletion observed in the troposphere?

**Answer from B (simulated):**  
*Based on topics in B's papers and vector search across their abstract data.*

---

## 🔮 Future Plans

- Improve citation tracing with full PDF parsing
- Streamlit interface for live exploration
- Generate multiple questions and answers with citations

---

## 🧠 Acknowledgements

- Semantic Scholar API
- LangChain + OpenAI
- ChromaDB for vector search

