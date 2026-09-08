# HealthHive

HealthHive is a safety intelligence website for turning unsafe-act, unsafe-condition and near-miss reports into prioritised SIF prevention work.

## Quick demo

Open `index.html` directly in a modern browser. No build step or web server is required for the interactive demo. Choose **Worker** to submit a multilingual, voice-assisted report, or **Supervisor** to use the dashboard, review queue, density view and closure verification. The direct-open demo stores reports in the browser's local report register, so a Worker submission persists across sign-out and is visible after signing in as a Supervisor on the same browser. The deployed React version registers users and saves reports in PostgreSQL through the API.

Demo sign-in accepts any name and a passcode of at least four characters. The role boundary is enforced in the UI: workers never receive dashboard navigation.

## Repository layout

```
index.html                 Direct-open, self-contained prototype
assets/
  styles.css               Responsive design system
  app.js                   Demo data, UI and browser speech integration
backend/
  app/
    main.py                FastAPI endpoints and prompt-style classifier
    models.py              SQLAlchemy data models
    schemas.py             API request/response models
    database.py            PostgreSQL configuration
  requirements.txt
  .env.example
  database/schema.sql      Standalone PostgreSQL schema and prototype sites
frontend-react/
  src/                     React implementation starter for production
  package.json
```

## Voice input and languages

The prototype uses the browser's Web Speech API (`SpeechRecognition`/`webkitSpeechRecognition`) in place of Pashmi. Chrome and Edge over HTTPS generally provide the best experience. Voice can be set to English, Hindi, Assamese or Bengali. The browser asks for microphone permission; speech text is placed in the report field and is saved with the report when submitted. When speech recognition is unavailable, the report form remains fully usable by typing. Translation is represented by a clear preview label in the demo; production should connect an approved translation provider or organization service.

## Full deployment

### Backend

1. Create a PostgreSQL database (Supabase works well for a prototype).
2. In `backend`, create `.env` from `.env.example` and set `DATABASE_URL`.
3. Install dependencies: `pip install -r requirements.txt`
4. Start: `uvicorn app.main:app --reload --port 8000`

The API documentation will be at `http://localhost:8000/docs`.

### Database master records

PostgreSQL is the master system of record for deployed use. The API creates `users`, `sites`, and `reports` tables on first startup. `POST /users/register` creates or safely returns an existing Worker or Supervisor record using its unique employee ID. Reports can be linked to the registered user through `reporter_id`. A production deployment should put organization SSO or a proper password-hash based authentication service in front of this endpoint.

If preferred, create the database manually first by running `backend/database/schema.sql` in Supabase SQL Editor, pgAdmin, or `psql`.

### React frontend

1. In `frontend-react`, run `npm install`.
2. Set `VITE_API_URL=http://localhost:8000` in `.env`.
3. Run `npm run dev`, or `npm run build` for a deployable static bundle.

Deploy the frontend to Vercel/Netlify and the API to Render or another service. Set CORS origins in `backend/app/main.py` to the final frontend domain.

## Prototype classifier note

The included classifier is intentionally explainable and deterministic so judges can inspect it. It identifies likely SIF exposure, IOGP Life-Saving Rule signals and precursor phrases from report text, then sends low-confidence reports to human review. Replace `classify_report` with an approved prompt-model service before operational use. AI assists prioritisation only; a qualified supervisor makes the final safety decision.

## Safety and privacy

This is a demonstration prototype, not a safety-management system of record. Do not submit real incident reports or personally sensitive data to the demo. Validate classifications, access control, audit trails, retention and escalation rules with the organization before deployment.
