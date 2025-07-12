'''
gameboard.py
Contains GameBoard class handling Gomoku game logic and win checking.
'''
class GameBoard:
    """Manages the Gomoku game state and win detection."""
    def __init__(self, size=15):
        """Initialize game board with given size (default 15x15)."""
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = 1
        self.game_over = False
    def reset(self):
        """Reset the board to initial state."""
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 1
        self.game_over = False
    def make_move(self, row, col):
        """
        Place a stone for current player if position is valid.
        Returns True if move was successful.
        """
        if (row < 0 or row >= self.size or col < 0 or col >= self.size):
            return False
        if not self.game_over and self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            return True
        return False
    def check_win(self, row, col):
        """Check if last move caused a win. Returns boolean."""
        player = self.current_player
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Horizontal, Vertical, Diagonals
        for dx, dy in directions:
            count = 1
            # Check in positive direction
            x, y = row + dx, col + dy
            while 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == player:
                count += 1
                x += dx
                y += dy
            # Check in negative direction
            x, y = row - dx, col - dy
            while 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == player:
                count += 1
                x -= dx
                y -= dy
            if count >= 5:
                self.game_over = True
                return True
        return False
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 3 - self.current_player  # Alternates between 1 and 2
    def is_board_full(self):
        """Check if the board is completely filled with stones."""
        for row in self.board:
            if 0 in row:
                return False
        return True