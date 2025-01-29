import chess.engine
import pandas as pd
from chess_analyzer.config import STOCKFISH_PATH
from tqdm import tqdm
import traceback

def analyze_game(moves_df, depth=18, time_limit=1):
    """Analyze game moves with Stockfish"""
    try:
        engine = chess.engine.SimpleEngine.popen_uci(str(STOCKFISH_PATH))
    except Exception as e:
        raise RuntimeError(f"Failed to start Stockfish: {str(e)}") from e

    analysis = []
    board = chess.Board()
    
    try:
        for idx, row in tqdm(moves_df.iterrows(), total=len(moves_df)):
            move_str = row['move'].replace('#', '') 
            try:
                # Handle pawn promotions
                if '=' in move_str:
                    move_part, promotion = move_str.split('=')
                    base_move = board.parse_san(move_part)
                    move = chess.Move(
                        from_square=base_move.from_square,
                        to_square=base_move.to_square,
                        promotion=chess.PIECE_SYMBOLS.index(promotion.lower())
                    )
                else:
                    move = board.parse_san(move_str)
                    
            except (chess.IllegalMoveError, ValueError) as e:
                analysis.append({"cpl": 0, "best_move": "", "is_blunder": False})
                board.push(chess.Move.null()) 

            try:
                # Configure engine for better performance
                engine.configure({"Hash": 512, "Threads": 2})
                info = engine.analyse(
                    board,
                    chess.engine.Limit(depth=depth, time=time_limit),
                    info=chess.engine.INFO_ALL
                )
                
                # Handle mate scores properly
                if info['score'].is_mate():
                    cpl = 10000 if info['score'].white().mate() > 0 else -10000
                else:
                    cpl = info['score'].relative.score(mate_score=10000)
                
                best_move = board.san(info['pv'][0]) if info['pv'] else ""
                
            except Exception as e:
                print(f"Error analyzing move {move_str}: {str(e)}")
                cpl = 0
                best_move = ""

            analysis.append({
                'cpl': abs(int(cpl)) if cpl is not None else 0,
                'best_move': best_move,
                'is_blunder': abs(cpl) > 200 if cpl is not None else False
            })
            
            try:
                board.push(move)
            except AssertionError:
                board.push(chess.Move.null())

    except Exception as e:
        traceback.print_exc()
        raise RuntimeError(f"Analysis failed: {str(e)}") from e
        
    finally:
        engine.quit()
    
    return pd.concat([moves_df, pd.DataFrame(analysis)], axis=1)