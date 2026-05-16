from agents.summarizer_agent import summarize_ticket

from agents.routing_agent import route_ticket

from agents.prediction_agent import predict_resolution_time

from agents.response_agent import generate_response

from rag.retriever import retrieve_similar_tickets


def master_agent(ticket):

    print("\n" + "=" * 60)
    print("MULTI-AGENT AI SUPPORT ANALYSIS")
    print("=" * 60)

    # ---------------------------------------------------
    # 1. Summarizer Agent
    # ---------------------------------------------------

    summary = summarize_ticket(ticket)

    print("\n[1] Ticket Summary\n")

    print(summary)

    # ---------------------------------------------------
    # 2. Routing Agent
    # ---------------------------------------------------

    department = route_ticket(ticket)

    print("\n[2] Routed Department\n")

    print(department)

    # ---------------------------------------------------
    # 3. Prediction Agent
    # ---------------------------------------------------

    prediction = predict_resolution_time(
        "high"
    )

    print("\n[3] Estimated Resolution Time\n")

    print(prediction)

    # ---------------------------------------------------
    # 4. RAG Retrieval Agent
    # ---------------------------------------------------

    results = retrieve_similar_tickets(ticket)

    print("\n[4] Similar Historical Tickets\n")

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")

        print("-" * 50)

        print(result.page_content[:400])

    # ---------------------------------------------------
    # 5. Response Generation Agent
    # ---------------------------------------------------

    final_response = generate_response(
        ticket,
        results
    )

    print("\n[5] AI Resolution Response\n")

    print(final_response)

    print("\n" + "=" * 60)


if __name__ == "__main__":

    user_ticket = input(
        "Enter customer support ticket:\n\n"
    )

    master_agent(user_ticket)