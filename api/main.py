from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agents.summarizer_agent import summarize_ticket
from agents.routing_agent import route_ticket
from agents.prediction_agent import predict_resolution_time
from agents.response_agent import generate_response

from rag.retriever import retrieve_similar_tickets


app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

class TicketRequest(BaseModel):
    ticket: str


@app.get("/")
def home():

    return {
        "message": "AI Support Backend Running"
    }


@app.post("/analyze-ticket")
def analyze_ticket(request: TicketRequest):

    ticket = request.ticket

    # Summary
    summary = summarize_ticket(ticket)

    # Routing
    department = route_ticket(ticket)

    # Prediction
    prediction = predict_resolution_time(
        "high"
    )

    # RAG Retrieval
    retrieved_results = retrieve_similar_tickets(
        ticket
    )

    similar_tickets = []

    for result in retrieved_results:

        similar_tickets.append(
            result.page_content[:400]
        )

    # AI Response
    ai_response = generate_response(
        ticket,
        retrieved_results
    )

    return {

        "summary": summary,

        "department": department,

        "estimated_resolution_time": prediction,

        "similar_tickets": similar_tickets,

        "ai_resolution": ai_response
    }