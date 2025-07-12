'''
Entry point for the Gomoku game application
'''
from gomoku_gui import GomokuGUI
from gomoku_game import GomokuGame
import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Gomoku Game")
    root.resizable(False, False)  # Prevent window resizing
    game = GomokuGame()
    gui = GomokuGUI(root, game)
    root.mainloop()
if __name__ == "__main__":
    main()