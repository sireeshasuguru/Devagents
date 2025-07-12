'''
Implements the graphical user interface for Gomoku using Tkinter
'''
import tkinter as tk
from tkinter import messagebox
class GomokuGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.cell_size = 40
        self.setup_ui()
    def setup_ui(self):
        self.canvas = tk.Canvas(self.master, 
                            width=self.game.board_size*self.cell_size,
                            height=self.game.board_size*self.cell_size)
        self.canvas.pack()
        self.draw_board()
        self.status_label = tk.Label(self.master, text="Player 1's Turn", font=('Arial', 14))
        self.status_label.pack(pady=10)
        self.reset_button = tk.Button(self.master, text="New Game", command=self.reset_game)
        self.reset_button.pack(pady=5)
        self.canvas.bind("<Button-1>", self.handle_click)
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.game.board_size):
            start = i * self.cell_size
            self.canvas.create_line(0, start, self.canvas.winfo_width(), start)
            self.canvas.create_line(start, 0, start, self.canvas.winfo_height())
        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                if self.game.board[row][col] != 0:
                    self.draw_stone(row, col)
    def draw_stone(self, row, col):
        x = col * self.cell_size + self.cell_size//2
        y = row * self.cell_size + self.cell_size//2
        color = "black" if self.game.board[row][col] == 1 else "white"
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill=color, outline="black")
    def handle_click(self, event):
        if self.game.game_over:
            return
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < self.game.board_size and 0 <= col < self.game.board_size:
            if self.game.make_move(row, col):
                self.draw_stone(row, col)
                self.update_status()
            else:
                messagebox.showwarning("Invalid Move", "This position is already occupied!")
    def update_status(self):
        if self.game.game_over:
            if self.game.winner is not None:  # Check winner state first
                winner = "Player 1" if self.game.winner == 1 else "Player 2"
                self.status_label.config(text=f"{winner} Wins!")
                messagebox.showinfo("Game Over", f"{winner} wins the game!")
            else:
                self.status_label.config(text="Game Draw!")
                messagebox.showinfo("Game Over", "The game is a draw!")
        else:
            player = "Player 1" if self.game.current_player == 1 else "Player 2"
            self.status_label.config(text=f"{player}'s Turn")
    def reset_game(self):
        self.game.reset_game()
        self.draw_board()
        self.status_label.config(text="Player 1's Turn")