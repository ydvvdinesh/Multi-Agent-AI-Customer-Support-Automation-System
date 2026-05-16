//instructions for first time user 
How to run - Always run backend first:
uvicorn api.main:app --reload
then run your index file 

How Your Project Works 🚀

Your project is:

Multi-Agent AI Customer Support Automation System

It automates customer support ticket handling using:

AI agents
semantic search
RAG
vector database
FastAPI backend
FULL PROJECT FLOW
Customer Ticket
       ↓
FastAPI Backend
       ↓
Master Agent
       ├── Summarizer Agent
       ├── Routing Agent
       ├── Prediction Agent
       ├── RAG Retrieval Agent
       └── Response Agent
               ↓
Final AI Response
STEP-BY-STEP WORKING
1. User Sends Ticket

Example:

payment ssl issue

This goes into:

api/main.py

through API endpoint:

POST /analyze-ticket
2. API Calls Master Agent

Inside:

api/main.py

your backend calls:

master_agent(ticket)
3. Master Agent Controls Everything

File:

agents/master_agent.py

This is the MAIN BRAIN of your system.

It orchestrates all agents one by one.

4. Summarizer Agent

File:

agents/summarizer_agent.py

Job:

reads long ticket
creates short summary

Example:

"software update failing..."
↓
"Software installation issue"
5. Routing Agent

File:

agents/routing_agent.py

Job:

decides department

Example:

payment issue
↓
Security / Payment Team
6. Prediction Agent

File:

agents/prediction_agent.py

Job:

estimates resolution time

Example:

Estimated Resolution: 3 Hours
7. RAG Retrieval Agent

Files:

rag/retriever.py
rag/vector_store.py
rag/embeddings.py

This is the MOST IMPORTANT AI part.

What It Does

It:

converts ticket into embeddings
searches FAISS vector DB
finds similar historical tickets

Example:

payment ssl issue
↓
retrieves old payment SSL failure tickets

This gives your AI:

historical memory/context
8. Response Agent

File:

agents/response_agent.py

Job:

generates final AI support response

Example:

Verify SSL certificate and TLS configuration.
9. Final API Response

Everything gets combined into JSON:

{
  "summary": "...",
  "department": "...",
  "prediction": "...",
  "similar_tickets": [...],
  "ai_response": "..."
}
VECTOR DATABASE WORKING

This is another important part.

File:
vector_store/build_vector_store.py

This file:

loads all support tickets
converts them into embeddings
stores vectors inside FAISS database
IMPORTANT

You run this ONLY ONCE initially.

Command:

python vector_store/build_vector_store.py

This creates:

vector_store/faiss_index/

which stores your AI memory database.

FILE EXPLANATION
agents/

Contains all AI agents.

File	Purpose
master_agent.py	Controls all agents
summarizer_agent.py	Summarizes tickets
routing_agent.py	Routes tickets
prediction_agent.py	Predicts resolution time
response_agent.py	Generates AI response
rag_agents.py	Tests RAG retrieval
rag/

Contains RAG pipeline.

File	Purpose
embeddings.py	Embedding model
retriever.py	Searches similar tickets
vector_store.py	Loads FAISS DB
vector_store/

Contains vector database creation.

File	Purpose
build_vector_store.py	Creates FAISS vector DB
data/tickets/

Contains historical support tickets.

These become:

AI knowledge base
api/

Contains FastAPI backend.

File	Purpose
main.py	API server