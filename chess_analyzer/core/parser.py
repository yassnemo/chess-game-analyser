import chess.pgn
import pandas as pd
from io import StringIO
from pathlib import Path

def parse_pgn(pgn_path):
    """Parse PGN file into DataFrame and metadata"""
    pgn = Path(pgn_path).read_text() if isinstance(pgn_path, (str, Path)) else pgn_path.read().decode()
    game = chess.pgn.read_game(StringIO(pgn))
    
    moves = []
    board = game.board()
    for move in game.mainline_moves():
        san_move = board.san(move)
        moves.append({
            "move": san_move,
            "turn": "White" if board.turn == chess.WHITE else "Black",
            "ply": board.ply(),
            "fen": board.fen()
        })
        board.push(move)
    
    metadata = {
        "white": game.headers.get("White", "Unknown"),
        "black": game.headers.get("Black", "Unknown"),
        "result": game.headers.get("Result", "*"),
        "date": game.headers.get("Date", ""),
        "eco": game.headers.get("ECO", "")
    }
    
    return pd.DataFrame(moves), metadata