import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
STOCKFISH_PATH = PROJECT_ROOT / "engine" / "stockfish.exe"

if not STOCKFISH_PATH.exists():
    raise FileNotFoundError(f"Stockfish not found at {STOCKFISH_PATH}")

DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"