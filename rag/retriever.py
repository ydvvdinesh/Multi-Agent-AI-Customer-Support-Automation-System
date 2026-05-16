from rag.vector_store import vectorstore

def retrieve_similar_tickets(query, k=2):

    results = vectorstore.similarity_search(
        query,
        k=k
    )

    return results