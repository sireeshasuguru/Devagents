```markdown
# Gomoku Game

A classic two-player strategy board game implemented in Python with Tkinter GUI

## Features

- 🎮 Traditional 15x15 Gomoku game board
- ♟️ Turn-based gameplay with black and white stones
- ✅ Automatic win detection (5-in-a-row)
- 🖱️ Mouse-controlled interface
- 🔄 One-click game reset functionality
- 📊 Real-time player turn indicator
- 🚫 Invalid move prevention and notifications

## Requirements

- Python 3.6 or higher
- Tkinter (normally included in standard Python installations)

## Installation

1. **Ensure Python is installed**  
   Verify installation by running in terminal:
   ```bash
   python --version
   ```
   You should see Python 3.x version information

2. **Download game files**  
   Ensure you have these files in the same directory:
   - `gameboard.py`
   - `main.py`

## How to Play

### Starting the Game
```bash
python main.py
```

### Game Interface
1. **Game Board**  
   - 15x15 grid displayed in a neutral background color
   - Click intersections to place stones

2. **Information Panel**  
   - Shows current player's turn at the bottom
   - Black moves first (Player 1)
   - White follows (Player 2)

3. **Controls**  
   - **New Game Button**: Resets the game at any time
   - **Grid Click**: Place your stone on valid intersections

### Game Rules
1. Players alternate placing stones of their color
2. First player to get 5 stones in a row wins
3. Winning line can be:
   - Horizontal
   - Vertical
   - Diagonal (both directions)
4. Game ends in draw if board fills completely

### Game Flow
1. Black player starts
2. Click desired intersection to place stone
3. Game automatically:
   - Checks for win condition
   - Detects draw situations
   - Switches player turns
4. Continue until win or draw

## Troubleshooting

- **"Invalid Move" popup**:
  - Clicked on occupied space
  - Clicked outside game board
  - Game has already concluded

- **Window not appearing**:
  - Verify Python/Tkinter installation
  - Check file permissions
  - Ensure both .py files are in same directory

- **Visual glitches**:
  - Resize window if elements appear misaligned
  - Restart game if artifacts persist

## Development Notes

This implementation uses:
- Pure Python with zero external dependencies
- Model-View-Controller pattern:
  - `GameBoard.py`: Game logic and state management
  - `main.py`: GUI presentation and user interaction

Enjoy your game of digital Gomoku! 🏆
```