import os

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

TICKET_FOLDER = "data/tickets"

documents = []

# Load all ticket files
for file in os.listdir(TICKET_FOLDER):

    if file.endswith(".txt"):

        path = os.path.join(TICKET_FOLDER, file)

        loader = TextLoader(path, encoding="utf-8")

        docs = loader.load()

        documents.extend(docs)

print(f"Loaded {len(documents)} ticket files")

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

split_docs = splitter.split_documents(documents)

print(f"Created {len(split_docs)} chunks")

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector DB
vectorstore = FAISS.from_documents(
    split_docs,
    embedding_model
)

# Save locally
vectorstore.save_local("vector_store/faiss_index")

print("Vector database created successfully!")