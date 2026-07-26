import os
import sys
from dotenv import load_dotenv
from groq import Groq
from data_loader import load_documents
from prompts import SYSTEM_PROMPT

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def run_research_agent(question, docs_dir="data/sources"):
    docs = load_documents(docs_dir)
    if not docs:
        return "No documents found in data/sources directory."

    # Build context from loaded files
    context = ""
    for doc in docs:
        context += f"\n--- SOURCE: {doc['source']} ---\n{doc['content']}\n"

    user_payload = f"Source Documents:\n{context}\n\nUser Question: {question}"

    # Call Groq API with Llama 3.3 model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_payload}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("\nEnter your research question: ")

    print("\n" + "="*50)
    print("RESEARCH SUMMARY & CITATIONS")
    print("="*50 + "\n")
    print(run_research_agent(user_query))
