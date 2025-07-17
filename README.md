# Scientific Dialogue Generator

This project generates simulated scientific conversations between two researchers, based on the abstracts of their published papers. It allows users to input two scientist names and then:

1. Searches Semantic Scholar for all papers authored by Scientist A and Scientist B.
2. Extracts and embeds the abstracts of their papers.
3. Automatically generates a research question that Scientist A might ask based on their research themes (optionally guided by a general topic).
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

Ensure you also have [ChromaDB](https://www.trychroma.com/) and the latest versions of `langchain`, `openai`, `tiktoken`, and `langchain-openai` installed.

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

This will save abstracts for the two scientists in the `papers/` folder.

### Step 2: Embed abstracts

```bash
python embed_papers.py
```

Chunks and stores vector embeddings in the `chroma_db/` folder.

### Step 3: Generate question and answer

```bash
python generate_dialogue.py
```

Generates a natural question and answer pair between Scientist A and Scientist B based on a shared research topic.

---

## 📁 Project Structure

```
Scientific-Dialogue-Generator/
├── papers/                 # Stored abstracts from Semantic Scholar
├── chroma_db/              # Vector DB created by Chroma
├── get_papers.py           # Fetch abstracts
├── embed_papers.py         # Create embeddings
├── generate_dialogue.py    # Generate Q&A dialogue
└── README.md
```

---

## 💡 Example Output

- **Scientist A:** Peter Blossey  
- **Scientist B:** Michael Pritchard

**Generated Question from A:**  
> How do global storm-resolving models accurately represent tropical cirrus clouds and deep convection processes in the Tropical Western Pacific compared to coarser-resolution climate models, and what are the implications for understanding cloud microphysics?

**Answer from B (simulated):**  
Global storm-resolving models (GSRMs) are able to explicitly resolve deep convection processes and capture the interaction between the scales of deep cumulus convection and large-scale dynamics in the atmosphere. This capability allows GSRMs to represent tropical cirrus clouds and convection processes more accurately compared to coarser-resolution climate models. The high resolution of GSRMs (kilometer-scale horizontal resolution) helps in capturing the details of orography and deep convection, which are usually parameterized in coarser-resolution models. This leads to a more realistic simulation of precipitation distributions and cloud microphysics in the Tropical Western Pacific region.

The implications of using GSRMs for understanding cloud microphysics are significant. By explicitly resolving convection, GSRMs provide a more detailed representation of cloud processes, including cirrus clouds, which play a crucial role in the Earth's radiation budget. The ability of GSRMs to simulate more realistic precipitation distributions and capture the vertical structure of tropical temperature change can enhance our understanding of how clouds respond to changes in sea surface temperature and CO2 concentration. This, in turn, can improve climate models and predictions related to cloud feedbacks and their impact on the Earth's climate system.

📚 Sources used:
- [abstract snippet]
- [abstract snippet]
- [abstract snippet]
- [abstract snippet]

---

## 🔮 Future Plans

- Improve citation tracing with full PDF parsing
- Add topic guidance for targeted question generation
- Streamlit interface for live exploration
- Generate multiple questions and answers with citations

---

## 🧠 Acknowledgements

- Semantic Scholar API
- LangChain + OpenAI
- ChromaDB for vector search
