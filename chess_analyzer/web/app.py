import streamlit as st 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from chess_analyzer.core.parser import parse_pgn
from chess_analyzer.core.analyzer import analyze_game
from chess_analyzer.core.visualizer import plot_accuracy, plot_heatmap

st.set_page_config(page_title="Chess Analyzer", layout="wide")

def main():
    st.title("♟️ Chess Game Analyzer")
    
    uploaded_file = st.file_uploader("Upload PGN File", type="pgn")
    
    if uploaded_file:
        with st.spinner("Analyzing game..."):
            try:
                moves_df, metadata = parse_pgn(uploaded_file)
                analysis = analyze_game(moves_df)
                
                # Display the metadata
                col1, col2, col3 = st.columns(3)
                col1.metric("White Player", metadata['white'])
                col2.metric("Black Player", metadata['black'])
                col3.metric("Result", metadata['result'])
                
                st.subheader("Move-by-Move Analysis")
                st.dataframe(analysis[['ply', 'move', 'cpl', 'best_move', 'is_blunder']])
                
                st.subheader("Game Insights")
                col1, col2 = st.columns(2)
                with col1:
                    st.pyplot(plot_accuracy(analysis))
                with col2:
                    st.pyplot(plot_heatmap(analysis))
                    
            except Exception as e:
                st.error(f"Error analyzing game: {str(e)}")
                st.code(traceback.format_exc())

if __name__ == "__main__":
    main()