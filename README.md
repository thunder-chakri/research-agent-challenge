[README.md](https://github.com/user-attachments/files/30391227/README.md)
\# Research Agent (with citations)



An end-to-end AI Research Agent built for the Rooman AI Challenge. It ingests source documents, synthesises answers to complex queries, and attaches precise inline source citations while guarding against hallucinations.



\---



\## 🛠️ Features

\- \*\*Strict Grounding:\*\* Answers questions \*only\* using provided document sources.

\- \*\*Source Citations:\*\* Appends exact document citations `\[file\_name]` to every factual claim.

\- \*\*Hallucination Safeguard:\*\* Clearly states when sources do not contain sufficient context to answer a query.

\- \*\*Multi-Format Support:\*\* Handles `.txt` and `.pdf` document files seamlessly.



\---



\## 🚀 Quickstart \& Setup Guide



\### 1. Prerequisites

\- Python 3.9+

\- Groq API Key (Free tier)



\### 2. Installation

```bash

git clone <YOUR\_GITHUB\_REPO\_URL>

cd research-agent-challenge

python -m venv venv

venv\\Scripts\\activate      # On Windows

\# source venv/bin/activate # On Linux/Mac

pip install -r requirements.txt

