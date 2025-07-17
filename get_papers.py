# Project: SciDialog - Scientist A asks, Scientist B answers

# Step 1: Input Scientist Names
scientist_a = "Peter Blossey"
scientist_b = " Michael Pritchard"

# Step 2: Search Papers for Each Scientist
# We'll use the Semantic Scholar API (https://api.semanticscholar.org/) for this
# You need an API key from Semantic Scholar (https://www.semanticscholar.org/product/api)

import requests
import os
from typing import List

API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
HEADERS = {"x-api-key": API_KEY}

BASE_URL = "https://api.semanticscholar.org/graph/v1"


def get_papers(author_name: str, limit: int = 50) -> List[str]:
    """
    Return a list of abstracts from papers written by the given author.
    """
    search_url = f"{BASE_URL}/author/search?query={author_name}&limit=1"
    resp = requests.get(search_url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    if not data["data"]:
        raise ValueError(f"Author '{author_name}' not found.")
    author_id = data["data"][0]["authorId"]

    papers_url = f"{BASE_URL}/author/{author_id}/papers?fields=title,abstract,year&limit={limit}"
    papers_resp = requests.get(papers_url, headers=HEADERS)
    papers_resp.raise_for_status()
    papers_data = papers_resp.json()["data"]

    abstracts = [f"Title: {p['title']}\nYear: {p['year']}\nAbstract: {p.get('abstract', '')}" for p in papers_data if p.get("abstract")]
    return abstracts


# Step 3: Save abstracts for each scientist to local files
a_abstracts = get_papers(scientist_a)
b_abstracts = get_papers(scientist_b)

with open("papers/papers_A.txt", "w") as f:
    f.write("\n\n".join(a_abstracts))

with open("papers/papers_B.txt", "w") as f:
    f.write("\n\n".join(b_abstracts))

print(f"✅ Downloaded and saved abstracts for {scientist_a} and {scientist_b}.")

