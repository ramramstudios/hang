from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uuid import uuid4
import os
import random
import httpx
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
OMDB_API_KEY = os.getenv("IMDB_API_KEY")

app = FastAPI()

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load words
with open("words.txt") as f:
    WORDS = [w.strip().upper() for w in f if len(w.strip()) >= 3]

GAMES = {}
MAX_WRONG = 6

def clean_title(title: str) -> str:
    title = title.upper()
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    cleaned = ''.join(c for c in title if c in allowed)
    return ' '.join(cleaned.split())


def fetch_random_movie() -> str:
    """Fetch a random movie title from OMDb or fall back to local words."""
    if not OMDB_API_KEY:
        return random.choice(WORDS)

    for _ in range(3):
        try:
            page = random.randint(1, 5)
            resp = httpx.get(
                f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s=movie&type=movie&page={page}",
                timeout=5,
            )
            data = resp.json()
            results = data.get("Search") or []
            if results:
                title = random.choice(results).get("Title", "")
                cleaned = clean_title(title)
                if cleaned:
                    return cleaned
        except Exception:
            pass
    return random.choice(WORDS)

class NewGameResponse(BaseModel):
    gameId: str
    length: int
    maxWrong: int
    masked: str

class GuessRequest(BaseModel):
    gameId: str
    letter: str

class GuessResponse(BaseModel):
    correct: bool
    positions: list[int]
    wrongGuesses: int
    gameOver: bool
    won: bool
    word: str | None = None

@app.post("/api/new-game", response_model=NewGameResponse)
def new_game():
    game_id = str(uuid4())
    word = fetch_random_movie()
    GAMES[game_id] = {"word": word, "wrong": 0, "guessed": []}
    masked = ''.join('_' if c != ' ' else ' ' for c in word)
    return NewGameResponse(gameId=game_id, length=len(word), maxWrong=MAX_WRONG, masked=masked)

@app.post("/api/guess", response_model=GuessResponse)
def guess(req: GuessRequest):
    game = GAMES.get(req.gameId)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    letter = req.letter.upper()
    if letter not in game["guessed"]:
        game["guessed"].append(letter)
        if letter not in game["word"]:
            game["wrong"] += 1

    positions = [i for i, c in enumerate(game["word"]) if c == letter]
    won = all(c in game["guessed"] for c in game["word"])
    game_over = won or (game["wrong"] >= MAX_WRONG)

    response = GuessResponse(
        correct=letter in game["word"],
        positions=positions,
        wrongGuesses=game["wrong"],
        gameOver=game_over,
        won=won,
    )
    if game_over:
        response.word = game["word"]
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
