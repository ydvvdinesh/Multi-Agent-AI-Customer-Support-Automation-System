from langchain_community.vectorstores import FAISS

from rag.embeddings import embedding_model

vectorstore = FAISS.load_local(
    "vector_store/faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)