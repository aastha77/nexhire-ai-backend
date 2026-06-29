# 🚀 NexHire AI Backend

NexHire AI Backend is an AI-powered recruitment engine built with **FastAPI** that helps recruiters find the most relevant candidates using semantic search and intelligent ranking.

The system analyzes hiring requirements, matches them with candidate profiles, calculates AI similarity scores, and provides explainable hiring recommendations.

---

## ✨ Features

- AI-powered candidate search
- Semantic matching between job descriptions and profiles
- Intelligent candidate ranking
- AI confidence scoring
- Explainable hiring recommendations
- FastAPI REST API
- High-speed candidate retrieval
- Production-ready backend deployment

---

## 🧠 How NexHire AI Works

```

Job Requirement Input

```
    ↓
```

AI Semantic Analysis

```
    ↓
```

Candidate Vector Matching

```
    ↓
```

Ranking Engine

```
    ↓
```

Top AI Recommended Candidates

```
    ↓
```

Explainable Hiring Insights

```

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn
- Pandas
- Semantic Search
- Vector Similarity Matching
- AI Ranking Engine

---

## 📂 Project Structure

```

nexhire-ai-backend

│
├── api.py
│     └── FastAPI application & API routes
│
├── engine/
│     └── AI search and ranking logic
│
├── output/
│     └── Processed candidate results
│
├── requirements.txt
│
├── Procfile
│
└── .gitignore

```

---

# 🔥 API Documentation

## Search Candidates

### Endpoint

```

POST /search

````

### Request Body

```json
{
  "description": "Senior Python engineer with FAISS Django AWS experience"
}
````

### Response Example

```json
{
  "candidates": [
    {
      "candidate_id": "CAND_001",
      "current_title": "AI Engineer",
      "ai_score": 0.96
    }
  ]
}
```

---

# 🚀 Run Locally

Clone repository:

```bash
git clone https://github.com/aastha77/nexhire-ai-backend.git
```

Move into project:

```bash
cd nexhire-ai-backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn api:app --reload
```

Backend will run at:

```
http://localhost:8000
```

---

# 🌐 Deployment

Backend is deployed using:

* Render

Live API:

```
https://nexhire-ai-backend.onrender.com
```

---

# 🎯 Use Case

NexHire AI helps companies reduce hiring time by automatically discovering suitable candidates and providing AI-driven insights for better recruitment decisions.

---

# 🤖 About NexHire AI

NexHire AI transforms traditional recruitment into an intelligent hiring workflow using AI, semantic search, and explainable candidate intelligence.

Built with ❤️ using FastAPI + AI

```
