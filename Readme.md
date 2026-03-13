# UISS – UNASAT Intelligent Support System

UISS (UNASAT Intelligent Support System) is een AI-ondersteund vraag-en-antwoord systeem voor studenten en medewerkers. Het systeem combineert een webinterface, een FastAPI backend, een MySQL database en een lokaal Large Language Model via Ollama.

De architectuur ondersteunt zowel **lokale development** als **Docker-gebaseerde deployment**.

---

# Architectuur

Het systeem bestaat uit vier services:

* **Frontend** – Webinterface voor gebruikers
* **Backend** – API gebouwd met FastAPI
* **MySQL** – Database voor conversaties, logs en gebruikers
* **Ollama** – Local LLM runtime voor AI antwoorden

```
User
  ↓
Frontend
  ↓
Backend (FastAPI API)
  ↓
RAG + Database
  ↓
Ollama (LLM)
```

---

# Projectstructuur

```
UISS
 ├ backend
 │   ├ app
 │   ├ requirements.txt
 │   └ main.py
 │
 ├ frontend
 │   ├ package.json
 │   └ src
 │
 ├ docker-compose.yml
 ├ backend.Dockerfile
 └ frontend.Dockerfile
```

---

# Vereisten

Installeer eerst:

* Docker
* Docker Compose
* Git
* Node.js (alleen nodig voor lokale frontend development)
* Python 3.11 (alleen nodig voor lokale backend development)

---

# Installatie (Docker – aanbevolen)

## 1. Repository clonen

```
git clone <repository-url>
cd UISS
```

---

## 2. Containers bouwen en starten

Start alle services:

```
docker compose up --build
```

Dit start automatisch:

* frontend container
* backend container
* MySQL database
* Ollama AI server

---

## 3. Ollama model downloaden

Wanneer de containers draaien moet het AI model eenmalig worden gedownload:

```
docker exec -it uiss_ollama ollama pull mistral
```

Of bijvoorbeeld:

```
docker exec -it uiss_ollama ollama pull llama3
```

---

## 4. Controleer of alles werkt

Open de volgende URL's in je browser:

Frontend

```
http://localhost:3000
```

Backend API

```
http://localhost:8000
```

API documentatie

```
http://localhost:8000/docs
```

Ollama API

```
http://localhost:11434
```

---

# Database configuratie

De MySQL container gebruikt standaard:

```
Database: uiss_db
User: uiss_user
Password: uiss_password
Port: 3306
```

Deze waarden kunnen aangepast worden in:

```
docker-compose.yml
```

---

# Environment configuratie

De backend gebruikt environment variables.

Voor Docker deployment:

```
backend/.env.docker
```

Voor lokale development:

```
backend/.env.local
```

Belangrijke variabelen:

```
SECRET_KEY=your_secret_key

DB_HOST=mysql
DB_PORT=3306
DB_USER=uiss_user
DB_PASS=uiss_password
DB_NAME=uiss_db

OLLAMA_URL=http://ollama:11434/api/generate
LOCAL_MODEL_NAME=mistral
```

---

# Backend lokaal starten (zonder Docker)

Ga naar de backend map:

```
cd backend
```

Maak een virtual environment:

```
python -m venv venv
```

Activeer de environment:

Windows:

```
venv\Scripts\activate
```

Linux/Mac:

```
source venv/bin/activate
```

Installeer dependencies:

```
pip install -r requirements.txt
```

Start de API:

```
uvicorn app.main:app --reload
```

API beschikbaar op:

```
http://localhost:8000
```

---

# Frontend lokaal starten

Ga naar de frontend map:

```
cd frontend
```

Installeer dependencies:

```
npm install
```

Start development server:

```
npm run dev
```

Frontend beschikbaar op:

```
http://localhost:5173
```

---

# AI functionaliteit

De AI gebruikt:

* Retrieval Augmented Generation (RAG)
* Document search
* Local LLM via Ollama

Proces:

```
User vraag
↓
Document search (RAG)
↓
Context genereren
↓
Prompt naar LLM
↓
AI antwoord
```

---

# Security features

Het systeem bevat meerdere beveiligingslagen:

* Prompt injection detectie
* Input sanitization
* Admin authentication (JWT)
* Security event logging
* Monitoring dashboard

---

# Monitoring endpoints

Admin endpoints:

```
/admin
/admin/monitor
/admin/logs
/admin/security
/admin/ai-metrics
```

---

# Development tips

Herstart containers wanneer code verandert:

```
docker compose down
docker compose up --build
```

Logs bekijken:

```
docker compose logs backend
```

MySQL container openen:

```
docker exec -it uiss_mysql mysql -u uiss_user -p
```

---

# Stoppen van het systeem

```
docker compose down
```

Alle data blijft behouden via Docker volumes.

---

# Licentie

Dit project is ontwikkeld voor academisch gebruik binnen UNASAT.
