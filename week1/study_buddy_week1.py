from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load API key from .env
load_dotenv()

# Read markdown notes
with open("my_notes.md", "r", encoding="utf-8") as file:
    notes = file.read()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

print("Study Buddy Ready!")
print("Type 'exit' to quit.\n")

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    prompt = f"""
You are a study assistant.

Here are the notes:

{notes}

Answer the following question using only the notes above.

Question:
{question}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    print("\nAnswer:")
    print(response.content)
    print()