from pathlib import Path
import os

# Explicit Windows path configuration
STOCKFISH_PATH = Path(__file__).parent.parent / "engine" / "stockfish-windows-x86-64-avx2.exe"

if not STOCKFISH_PATH.exists():
    raise FileNotFoundError(f"""
    Stockfish not found at {STOCKFISH_PATH}
    Verify:
    1. File exists at above path
    2. Downloaded from stockfishchess.org
    3. No .txt extension on filename
    4. File not blocked by Windows (Right-click → Properties → Unblock)
    """)

DATA_DIR = Path(__file__).parent.parent / "data"
MODEL_DIR = Path(__file__).parent.parent / "models"