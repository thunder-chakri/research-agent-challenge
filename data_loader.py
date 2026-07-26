import os
from pypdf import PdfReader

def load_documents(docs_folder="data/sources"):
    documents = []
    if not os.path.exists(docs_folder):
        return documents

    for file_name in os.listdir(docs_folder):
        file_path = os.path.join(docs_folder, file_name)
        
        if file_name.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                documents.append({
                    "source": file_name,
                    "content": f.read()
                })
        elif file_name.endswith('.pdf'):
            reader = PdfReader(file_path)
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text and text.strip():
                    documents.append({
                        "source": f"{file_name} (Page {page_num + 1})",
                        "content": text
                    })
    return documents
