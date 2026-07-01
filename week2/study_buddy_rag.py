from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from sentence_transformers import SentenceTransformer

import faiss
import os

# ==========================================
# STEP 1: Load Notes
# ==========================================

print("\nLoading Document...\n")

with open("my_notes.md", "r", encoding="utf-8") as file:
    text = file.read()

print("DOCUMENT LOADED!")

# ==========================================
# STEP 2: Create Chunks
# ==========================================

raw_chunks = text.split("\n\n")

raw_chunks = [
    chunk.strip()
    for chunk in raw_chunks
    if len(chunk.strip()) > 10
]

chunks = []

chunk_size = 5

for i in range(0, len(raw_chunks), chunk_size):
    combined_chunk = "\n\n".join(raw_chunks[i:i+chunk_size])
    chunks.append(combined_chunk)

print(f"Total Chunks Created: {len(chunks)}")

if len(chunks) == 0:
    print("No chunks created!")
    exit()

# ==========================================
# STEP 3: Generate Embeddings
# ==========================================

print("\nGenerating Embeddings...\n")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = embedder.encode(
    chunks,
    convert_to_numpy=True
)

print("Embeddings Generated!")
print("Total Embeddings:", len(embeddings))
print("Embedding Dimension:", len(embeddings[0]))

# ==========================================
# STEP 4: Create FAISS Index
# ==========================================

print("\nCreating FAISS Index...\n")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("FAISS Index Created!")
print("Vectors Stored:", index.ntotal)

# ==========================================
# STEP 5: Ask Question
# ==========================================

print("\nRetrieving Relevant Chunks...\n")

question = input("Ask a question: ").strip()

if question == "":
    print("Question cannot be empty!")
    exit()

# ==========================================
# STEP 6: Convert Question to Embedding
# ==========================================

question_embedding = embedder.encode(
    [question],
    convert_to_numpy=True
)

print("Question Embedding Created!")

# ==========================================
# STEP 7: Search FAISS
# ==========================================

k = 5

distances, indices = index.search(
    question_embedding,
    k
)

print("\nSearch Completed!")
print("Distances:", distances)
print("Indices:", indices)

# ==========================================
# STEP 8: Retrieve Chunks
# ==========================================

relevant_chunks = [
    chunks[idx]
    for idx in indices[0]
]

print("\nRelevant Chunks Found:\n")

for i, chunk in enumerate(relevant_chunks):
    print(f"Chunk {i+1}")
    print("-" * 50)
    print(chunk)
    print()

# ==========================================
# STEP 9: Load Gemini
# ==========================================

print("\nGenerating Final Answer...\n")

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("GOOGLE_API_KEY not found in .env file!")
    exit()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# ==========================================
# STEP 10: Create Context
# ==========================================

context = "\n\n".join(relevant_chunks)

print("Context Length:", len(context))

prompt = f"""
You are a helpful study assistant.

Use ONLY the information provided below.

Context:
{context}

Question:
{question}

Answer:
"""

# ==========================================
# STEP 11: Generate Answer
# ==========================================

response = llm.invoke(
    [HumanMessage(content=prompt)]
)

print("\nFinal Answer:\n")
print(response.content)