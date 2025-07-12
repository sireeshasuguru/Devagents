'''
Contains game logic and state management for Gomoku
'''
class GomokuGame:
    def __init__(self):
        self.board_size = 15
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False
        self.winner = None  # Track game outcome state
    def make_move(self, row, col):
        if self.game_over or self.board[row][col] != 0:
            return False
        self.board[row][col] = self.current_player
        if self.check_win(row, col):
            self.game_over = True
            self.winner = self.current_player  # Set winner when winning condition met
            return True
        if all(cell != 0 for row in self.board for cell in row):
            self.game_over = True
            self.winner = None  # Mark draw state
            return True
        self.current_player = 2 if self.current_player == 1 else 1
        return True
    def check_win(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.check_direction(row, col, dr, dc)
            count += self.check_direction(row, col, -dr, -dc)
            if count >= 5:
                return True
        return False
    def check_direction(self, row, col, dr, dc):
        player = self.board[row][col]
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < self.board_size and 0 <= c < self.board_size:
            if self.board[r][c] == player:
                count += 1
                r += dr
                c += dc
            else:
                break
        return count
    def reset_game(self):
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False
        self.winner = None  # Reset winner state