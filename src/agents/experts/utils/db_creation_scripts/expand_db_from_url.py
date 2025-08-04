from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Better than CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader


URL = "your URL goes here"
PERSISTENT_DIRECTORY = '../../expert_dbs/expert_db' # CHANGE THIS APPROPRIATELY

# Initialize embedding function (same as when you created the DB)
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# Load existing DB
db = Chroma(
    persist_directory=PERSISTENT_DIRECTORY,
    embedding_function=embedding_function
)

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

# Add new documents to existing collection
db.add_documents(documents=docs)

# IMPORTANT: Persist the changes
db.persist()

with open('db_logs.txt', 'a') as f:
    f.write(f'{URL} added to {PERSISTENT_DIRECTORY}')