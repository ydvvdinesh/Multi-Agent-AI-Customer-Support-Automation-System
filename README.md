# 🤖 Multi-Agent AI Customer Support Automation System

A **Multi-Agent AI Customer Support Automation System** that automatically analyzes customer support tickets, identifies the responsible department, predicts resolution time, retrieves similar historical tickets using **RAG + FAISS**, and generates an AI-powered support response.

The system is built using:

* 🤖 Multi-Agent AI Architecture
* 🔎 Semantic Search
* 🧠 RAG (Retrieval-Augmented Generation)
* 🗄️ FAISS Vector Database
* ⚡ FastAPI Backend
* 🌐 Web/API Frontend

---

# 🚀 Instructions for First-Time Users

## 1. Install Dependencies

Make sure Python is installed, then install the project's dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. Build the Vector Database — First Time Only

Before running the application for the first time, create the FAISS vector database from the historical support tickets.

Run:

```bash
python vector_store/build_vector_store.py
```

This processes the historical tickets, generates embeddings, and stores them in the FAISS database.

It creates:

```text
vector_store/faiss_index/
```

> ⚠️ **Important:** You only need to run `build_vector_store.py` initially, or whenever you update/rebuild the historical ticket dataset.

---

## 3. Start the Backend First

The **FastAPI backend must always be started before the frontend/index file**.

Run:

```bash
uvicorn api.main:app --reload
```

The API server will start locally.

Keep this terminal running.

---

## 4. Run the Frontend / Index File

After the backend is running, open another terminal and run your project's index/frontend file.

For example:

```bash
python index.py
```

> Replace `index.py` with the actual entry-point file used by your project.

---

# 🔄 How Your Project Works

The complete system follows this architecture:

```text
                    Customer Ticket
                           ↓
                    FastAPI Backend
                           ↓
                     Master Agent
                           ↓
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
     Summarizer        Routing          Prediction
       Agent             Agent             Agent
          └────────────────┼────────────────┘
                           ↓
                   RAG Retrieval Agent
                           ↓
                    FAISS Vector DB
                           ↓
                    Response Agent
                           ↓
                    Final AI Response
```

In simple terms:

**Customer Ticket → Analyze → Route → Predict → Retrieve Knowledge → Generate Response**

---

# 🧠 Step-by-Step Working

## 1️⃣ User Sends a Support Ticket

The user submits a customer support ticket.

Example:

```text
payment ssl issue
```

The request is received by:

```text
api/main.py
```

through the API endpoint:

```text
POST /analyze-ticket
```

---

## 2️⃣ FastAPI Calls the Master Agent

Inside:

```text
api/main.py
```

the backend sends the ticket to:

```text
master_agent(ticket)
```

The Master Agent then takes control of the entire AI workflow.

---

## 3️⃣ Master Agent — The Main Brain

File:

```text
agents/master_agent.py
```

The **Master Agent** is the central orchestrator of the system.

It coordinates the different specialized agents and ensures that the ticket passes through the required processing stages.

```text
Master Agent
     ↓
Summarizer
     ↓
Routing
     ↓
Prediction
     ↓
RAG Retrieval
     ↓
Response
```

---

# 4️⃣ Summarizer Agent

File:

```text
agents/summarizer_agent.py
```

### Purpose

Converts a long or complicated support ticket into a concise summary.

Example:

```text
Original Ticket:
"After installing the latest software update,
the application fails to start and shows an error..."

                     ↓

Summary:
"Software installation issue"
```

This gives the other agents a cleaner representation of the problem.

---

# 5️⃣ Routing Agent

File:

```text
agents/routing_agent.py
```

### Purpose

Determines which department or team should handle the ticket.

Example:

```text
Payment SSL Issue
       ↓
Security / Payment Team
```

The routing agent helps automatically direct the ticket to the appropriate support department.

---

# 6️⃣ Prediction Agent

File:

```text
agents/prediction_agent.py
```

### Purpose

Estimates how long the issue may take to resolve.

Example:

```text
Estimated Resolution Time:
3 Hours
```

This provides an expected resolution timeline for the support ticket.

---

# 7️⃣ RAG Retrieval Agent 🔎

Files:

```text
rag/retriever.py
rag/vector_store.py
rag/embeddings.py
```

This is one of the most important AI components of the system.

The RAG pipeline gives the AI access to **historical support-ticket knowledge**.

### How it works

The user's ticket:

```text
payment ssl issue
```

is converted into an **embedding**.

The system then performs semantic similarity search against the FAISS vector database.

```text
Customer Ticket
      ↓
Embedding Model
      ↓
Vector Representation
      ↓
FAISS Similarity Search
      ↓
Similar Historical Tickets
```

For example:

```text
payment ssl issue
        ↓
Similar historical tickets
        ↓
Previous SSL/payment failures
        ↓
Relevant solutions/context
```

This provides the AI with historical context rather than relying only on the current ticket.

---

# 8️⃣ Response Agent

File:

```text
agents/response_agent.py
```

### Purpose

Generates the final AI-powered customer support response.

The Response Agent uses information gathered from the previous agents and the RAG system.

Example:

```text
Verify the SSL certificate and TLS configuration.
Check whether the certificate has expired and
ensure that the correct certificate chain is installed.
```

---

# 9️⃣ Final API Response

After all agents complete their tasks, the backend combines the results into a structured response.

Example:

```json
{
  "summary": "Payment SSL issue",
  "department": "Security / Payment Team",
  "prediction": "3 Hours",
  "similar_tickets": [
    "...",
    "..."
  ],
  "ai_response": "Verify SSL certificate and TLS configuration."
}
```

This response is then returned by the FastAPI backend to the frontend/client.

---

# 🗄️ Vector Database Architecture

The project uses **FAISS** as the vector database for semantic retrieval.

The vector database is created using:

```text
vector_store/build_vector_store.py
```

This script:

1. Loads historical support tickets
2. Converts tickets into embeddings
3. Stores the embeddings in FAISS
4. Creates the searchable vector index

```text
Historical Support Tickets
            ↓
       Embedding Model
            ↓
      Vector Embeddings
            ↓
        FAISS Index
            ↓
       AI Knowledge Base
```

The resulting database is stored in:

```text
vector_store/faiss_index/
```

### ⚠️ Important

Run:

```bash
python vector_store/build_vector_store.py
```

**only during initial setup or when the historical dataset changes and the vector index needs to be rebuilt.**

You do **not** need to rebuild the vector database every time you start the application.

---

# 📁 Project Structure

```text
project/
│
├── agents/
│   ├── master_agent.py
│   ├── summarizer_agent.py
│   ├── routing_agent.py
│   ├── prediction_agent.py
│   ├── response_agent.py
│   └── rag_agents.py
│
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── vector_store/
│   ├── build_vector_store.py
│   └── faiss_index/
│
├── data/
│   └── tickets/
│
├── api/
│   └── main.py
│
├── index.py
├── requirements.txt
└── README.md
```

---

# 📂 Folder & File Explanation

## `agents/`

Contains the specialized AI agents responsible for different stages of ticket processing.

| File                  | Purpose                                 |
| --------------------- | --------------------------------------- |
| `master_agent.py`     | Controls and orchestrates all agents    |
| `summarizer_agent.py` | Summarizes customer tickets             |
| `routing_agent.py`    | Determines the appropriate department   |
| `prediction_agent.py` | Predicts estimated resolution time      |
| `response_agent.py`   | Generates the final support response    |
| `rag_agents.py`       | RAG-related testing/agent functionality |

---

## `rag/`

Contains the **Retrieval-Augmented Generation pipeline**.

| File              | Purpose                                     |
| ----------------- | ------------------------------------------- |
| `embeddings.py`   | Generates vector embeddings                 |
| `retriever.py`    | Searches for similar tickets                |
| `vector_store.py` | Loads and interacts with the FAISS database |

---

## `vector_store/`

Contains the vector database generation logic.

| File                    | Purpose                           |
| ----------------------- | --------------------------------- |
| `build_vector_store.py` | Creates the FAISS vector database |
| `faiss_index/`          | Stores the generated vector index |

---

## `data/tickets/`

Contains historical customer support tickets.

These historical tickets form the system's **AI knowledge base**.

They are converted into embeddings and stored in FAISS for semantic retrieval.

---

## `api/`

Contains the FastAPI backend.

| File      | Purpose                                              |
| --------- | ---------------------------------------------------- |
| `main.py` | Starts the API and exposes ticket-analysis endpoints |

The primary endpoint is:

```text
POST /analyze-ticket
```

---

# ⚡ Complete Startup Sequence

For a **first-time setup**, use:

```text
1. Install dependencies
        ↓
2. Build FAISS Vector Database
        ↓
3. Start FastAPI Backend
        ↓
4. Start Frontend / Index
```

Commands:

```bash
pip install -r requirements.txt
```

Then:

```bash
python vector_store/build_vector_store.py
```

Then start the backend:

```bash
uvicorn api.main:app --reload
```

Finally, in another terminal:

```bash
python index.py
```

---

# 🔁 For Normal Usage

Once the FAISS database has already been created, you generally **do not need to rebuild it**.

Just start the backend first:

```bash
uvicorn api.main:app --reload
```

Then start the frontend/index:

```bash
python index.py
```

---

# 🚀 One-Line Understanding

```text
Customer Ticket
      ↓
FastAPI
      ↓
Master Agent
      ↓
Specialized AI Agents
      ↓
RAG + FAISS Historical Knowledge
      ↓
Response Agent
      ↓
AI-Powered Customer Support Response
```

### In simple words:

> **Your project uses multiple specialized AI agents together with RAG and a FAISS vector database to automatically understand, classify, predict, retrieve knowledge for, and respond to customer support tickets.**
