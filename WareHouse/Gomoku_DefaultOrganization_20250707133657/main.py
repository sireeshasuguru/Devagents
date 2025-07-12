'''
main.py
Main application file for Gomoku game using Tkinter GUI.
'''
import tkinter as tk
from tkinter import messagebox
from gameboard import GameBoard
class GomokuGUI:
    """Handles the graphical interface and user interactions."""
    def __init__(self, master):
        """Initialize GUI components and game board."""
        self.master = master
        self.master.title("Gomoku Game")
        self.board_size = 15
        self.cell_size = 40
        self.canvas_size = self.board_size * self.cell_size
        self.game = GameBoard(self.board_size)
        # Create canvas
        self.canvas = tk.Canvas(master, width=self.canvas_size, height=self.canvas_size, bg='burlywood3')
        self.canvas.pack()
        self.draw_board()
        # Info panel
        self.info_label = tk.Label(master, text=f"Current Player: {self.game.current_player}", font=('Arial', 14))
        self.info_label.pack()
        # Reset button
        self.reset_btn = tk.Button(master, text="New Game", command=self.reset_game)
        self.reset_btn.pack(pady=10)
        # Bind click event
        self.canvas.bind("<Button-1>", self.handle_click)
    def draw_board(self):
        """Draw the game board grid lines."""
        for i in range(self.board_size):
            start = i * self.cell_size
            self.canvas.create_line(start, 0, start, self.canvas_size)  # Vertical
            self.canvas.create_line(0, start, self.canvas_size, start)  # Horizontal
    def handle_click(self, event):
        """Handle player click event to place stones."""
        if self.game.game_over:
            return
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if 0 <= x < self.board_size and 0 <= y < self.board_size:
            if self.game.make_move(y, x):
                self.draw_stone(y, x)
                if self.game.check_win(y, x):
                    messagebox.showinfo("Game Over", f"Player {self.game.current_player} wins!")
                    self.info_label.config(text=f"Player {self.game.current_player} wins!")
                else:
                    if self.game.is_board_full():
                        messagebox.showinfo("Game Over", "Draw! No more moves.")
                        self.game.game_over = True
                        self.info_label.config(text="Game Over: Draw!")
                    else:
                        self.game.switch_player()
                        self.info_label.config(text=f"Current Player: {self.game.current_player}")
            else:
                messagebox.showinfo("Invalid Move", "Cell already occupied!")
        else:
            messagebox.showinfo("Invalid Move", "Click inside the game board!")
    def draw_stone(self, row, col):
        """Draw a stone at specified grid position."""
        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2
        color = 'black' if self.game.current_player == 1 else 'white'
        radius = self.cell_size // 2 - 5  # Dynamic radius based on cell size
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, 
                               fill=color, outline='black')
    def reset_game(self):
        """Reset the game state and UI."""
        self.game.reset()
        self.canvas.delete("all")
        self.draw_board()
        self.info_label.config(text=f"Current Player: {self.game.current_player}")
if __name__ == "__main__":
    root = tk.Tk()
    app = GomokuGUI(root)
    root.mainloop()