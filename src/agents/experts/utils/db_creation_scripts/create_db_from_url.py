from langchain.text_splitter import RecursiveCharacterTextSplitter  # Better than CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

from langchain_community.document_loaders import WebBaseLoader

URL = "your URL goes here"
PERSISTENT_DIRECTORY = 'expert_dbs/expert_db' # CHANGE THIS APPROPRIATELY

loader = WebBaseLoader(URL)
data = loader.load()

# 1. Use RecursiveCharacterTextSplitter instead - handles long texts better
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]  # Try to split on paragraphs first
)

# 2. Clean your data first
def clean_documents(data):
    return [doc for doc in data if doc.page_content.strip()]  # Remove empty documents

cleaned_data = clean_documents(data)
docs = text_splitter.split_documents(cleaned_data)

# 3. Verify documents before embedding
print(f"Total documents after splitting: {len(docs)}")
for i, doc in enumerate(docs[:3]):  # Inspect first few
    print(f"Doc {i} length: {len(doc.page_content)}")
    print(f"Metadata: {doc.metadata}")

# 4. Create DB with error handling
try:
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(
        documents=docs,
        embedding=embedding_function,
        persist_directory=PERSISTENT_DIRECTORY
    )
    print("Database created successfully!")
except Exception as e:
    print(f"Error creating DB: {e}")
    # Inspect problematic documents
    for i, doc in enumerate(docs):
        if not doc.page_content or len(doc.page_content) > 2000:
            print(f"Problematic doc {i}: Length={len(doc.page_content)}")