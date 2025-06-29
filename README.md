# Hangman Game

This project contains a simple Hangman game with a Svelte/Vite front-end and a FastAPI back-end.

## Back-end

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Front-end

```bash
cd frontend
npm install
npm run dev
```

The Vite dev server proxies API requests to the FastAPI server running on `localhost:8000`.
