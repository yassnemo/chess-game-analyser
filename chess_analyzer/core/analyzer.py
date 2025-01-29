import chess.engine
import pandas as pd
from chess_analyzer.config import STOCKFISH_PATH
from tqdm import tqdm
import traceback

def analyze_game(moves_df, depth=18, time_limit=0.1):
    """Analyze game moves with Stockfish"""
    try:
        engine = chess.engine.SimpleEngine.popen_uci(str(STOCKFISH_PATH))
    except Exception as e:
        raise RuntimeError(f"Failed to start Stockfish: {str(e)}") from e

    analysis = []
    board = chess.Board()
    
    try:
        for idx, row in tqdm(moves_df.iterrows(), total=len(moves_df)):
            try:
                move = board.parse_san(row['move'])
            except chess.IllegalMoveError:
                analysis.append({"cpl": 0, "best_move": "", "is_blunder": False})
                board.push(chess.Move.null())  
                continue

            try:
                info = engine.analyse(
                    board,
                    chess.engine.Limit(depth=depth, time=time_limit)
                )
                cpl = info['score'].relative.score(mate_score=10000)
                best_move = board.san(info['pv'][0]) if info['pv'] else ""
            except Exception as e:
                print(f"Error analyzing move {row['move']}: {str(e)}")
                cpl = 0
                best_move = ""

            analysis.append({
                'cpl': abs(cpl) if cpl else 0,
                'best_move': best_move,
                'is_blunder': abs(cpl) > 200 if cpl else False
            })
            
            board.push(move)
            
    except Exception as e:
        traceback.print_exc()
        raise RuntimeError(f"Analysis failed: {str(e)}") from e
        
    finally:
        engine.quit()
    
    return pd.concat([moves_df, pd.DataFrame(analysis)], axis=1)