```markdown
# Gomoku Game Manual

## Overview
Gomoku is a traditional strategy board game where two players alternate placing stones on a 15x15 grid, aiming to be the first to form an unbroken line of five stones. This digital implementation features a graphical interface and follows standard Gomoku rules.

## System Requirements
- Python 3.6 or higher
- Tkinter (included in standard Python distribution)

## Installation
1. Ensure Python is installed:
   ```bash
   python --version
   ```
2. Download these files to the same directory:
   - `main.py`
   - `gomoku_game.py`
   - `gomoku_gui.py`

## How to Play
### Starting the Game
```bash
python main.py
```

### Game Interface
![GUI Description]
- **Game Board**: 15x15 grid for stone placement
- **Status Bar**: Shows current player's turn or game result
- **New Game Button**: Resets the game at any time

### Gameplay
1. **Taking Turns**
   - Player 1 (Black) always starts
   - Alternate placing stones by clicking grid intersections
   
2. **Placing Stones**
   - Click desired intersection
   - Valid moves: Empty intersections
   - Invalid moves show warning message

3. **Winning Condition**
   - First player to create 5-in-a-row (horizontal/vertical/diagonal)
   - Game automatically detects wins and declares winner

4. **Draw Condition**
   - Board filled completely with no winner
   - Game declares draw automatically

5. **New Game**
   - Click "New Game" button anytime to reset
   - Clears board and resets to Player 1

## Game Rules
- Standard Gomoku rules (no prohibited moves)
- Five-in-a-row wins immediately
- Stones cannot be moved once placed
- No undo functionality

## Features
- Clean graphical interface
- Real-time game state tracking
- Automatic win/draw detection
- Immediate visual feedback
- Cross-platform compatibility

## Troubleshooting
**Common Issues:**
- **Window not opening**: Ensure all files are in same directory
- **Clicks not registering**: 
  - Check if game is over (start new game)
  - Verify click is on empty intersection
- **Display issues**: Ensure screen resolution supports minimum 600x600 area

## Support
Contact support@chatdev.com for:
- Bug reports
- Feature requests
- Technical issues

---

**Enjoy your Gomoku experience!** 🎮
```