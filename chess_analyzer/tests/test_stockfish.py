import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import chess.engine
from chess_analyzer.config import STOCKFISH_PATH

def test_stockfish():
    try:
        engine = chess.engine.SimpleEngine.popen_uci(str(STOCKFISH_PATH))
        print("✅ Stockfish working! Version:", engine.id["name"])
        engine.quit()
        return True
    except Exception as e:
        print("❌ Stockfish failed:", str(e))
        return False

if __name__ == "__main__":
    test_stockfish()