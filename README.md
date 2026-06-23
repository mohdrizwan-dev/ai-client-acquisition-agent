# AI Client Acquisition Agent

A scalable AI-powered client acquisition operating system.

This repo is organized as a practical MVP first:

- Find leads that may need web, automation, or AI services
- Analyze their website/business profile
- Score the opportunity
- Generate a personalized outreach proposal
- Track leads, interactions, and follow-ups in a CRM dashboard

## Architecture

```text
frontend/  Next.js dashboard and CRM UI
backend/   FastAPI API, agents, workflows, database models
```

## MVP Flow

1. Add or discover a lead
2. Analyze the lead website
3. Score the lead
4. Generate a proposal
5. Approve outreach manually
6. Track responses and follow-ups

## Local Development

### Backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The API will run at `http://127.0.0.1:8000`.

If Windows fails while bootstrapping pip inside the venv, this fallback works:

```powershell
cd backend
python -m pip install -r requirements.txt --target .venv\Lib\site-packages
$env:PYTHONPATH=".venv\Lib\site-packages"
python -m uvicorn app.main:app --reload
```

### Frontend

```powershell
cd frontend
npm.cmd install
npm.cmd run dev
```

The app will run at `http://localhost:3000`.

## Safety Principles

- Human approval before sending outreach
- No aggressive scraping
- Rate limits and delays by default
- Store audit evidence before generating claims
- Respect each platform's terms and robots policies
