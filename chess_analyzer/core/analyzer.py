import chess.engine
import pandas as pd
from chess_analyzer.config import STOCKFISH_PATH
from tqdm import tqdm

def analyze_game(moves_df, depth=18, time_limit=0.1):
    """Analyze game moves with Stockfish"""
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    analysis = []
    
    board = chess.Board()
    for idx, row in tqdm(moves_df.iterrows(), total=len(moves_df)):
        try:
            move = board.parse_san(row['move'])
        except chess.IllegalMoveError:
            analysis.append({"cpl": 0, "best_move": "", "is_blunder": False})
            continue
            
        info = engine.analyse(
            board,
            chess.engine.Limit(depth=depth, time=time_limit)
        )
        
        cpl = info['score'].relative.score(mate_score=10000)
        best_move = board.san(info['pv'][0]) if info['pv'] else ""
        
        analysis.append({
            'cpl': abs(cpl) if cpl else 0,
            'best_move': best_move,
            'is_blunder': abs(cpl) > 200  # Blunder threshold
        })
        
        board.push(move)
    
    engine.quit()
    return pd.concat([moves_df, pd.DataFrame(analysis)], axis=1)