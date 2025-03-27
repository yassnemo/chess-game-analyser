# Chess Game Analyser

## Overview

Chess Game Analyser is a Python-based tool designed to analyze chess games from PGN (Portable Game Notation) files. It provides insights into gameplay, detects patterns, and assists players in improving their strategic decisions.


## Features

- **PGN File Parsing:** Reads and processes PGN files to extract game data.
- **Move Analysis:** Evaluates each move to identify strengths and weaknesses.
- **Pattern Detection:** Recognizes recurring strategies and tactics.
- **Visualization:** Generates visual representations of game progress and key moments.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yassnemo/chess-game-analyser.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd chess-game-analyser
   ```

3. **Install Required Dependencies:**
   Ensure you have Python installed. Then, install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your PGN Files:**
   Place your PGN files in the designated `pgn_files/` directory.

2. **Run the Analysis Script:**
   ```bash
   python analyze.py --file pgn_files/sample_game.pgn
   ```

3. **View Results:**
   - The tool will output move evaluations, blunder detections, and suggested improvements.
   - If visualization is enabled, a graphical representation of the game will be generated.

## Configuration

Modify `config.yaml` to adjust analysis settings, including:
- Depth of analysis
- Engine evaluation thresholds
- Visualization preferences

## Dependencies

- Python 3.7+
- `chess` (for PGN parsing and board representation)
- `matplotlib` (for visualizations)
- `stockfish` (for move evaluations, if enabled)

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

