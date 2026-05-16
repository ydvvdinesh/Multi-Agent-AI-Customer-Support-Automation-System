from rag.retriever import retrieve_similar_tickets


def rag_agent(query):

    results = retrieve_similar_tickets(query)

    print("\n" + "=" * 60)
    print("TOP MATCHING SUPPORT TICKETS")
    print("=" * 60)

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 60)

        # Show source file
        if "source" in result.metadata:
            print(f"Source File: {result.metadata['source']}")

        print("\nTicket Content:\n")

        print(result.page_content)

        print("\n" + "=" * 60)


if __name__ == "__main__":

    user_query = input("Ask support question: ")

    rag_agent(user_query)