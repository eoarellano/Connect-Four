from typing import List

class Board:

    def __init__(self, grid: List[List[str]], player: str):
        self.grid = grid
        self.player = player
        self.rows = 6
        self.cols = 7
    
    def get_valid_moves(self):
        return [col for col in range(self.cols) if self.grid[0][col] == 'O']
    
    def make_move(self, col: int) -> bool:
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == 'O':
                self.grid[row][col] = self.player
                return True
        return False
    
    def has_winner(self, piece: str) -> bool:
        # Check horizontal locations for win
        for c in range(self.cols - 3):
            for r in range(self.rows):
                if (self.grid[r][c] == piece and self.grid[r][c+1] == piece and
                    self.grid[r][c+2] == piece and self.grid[r][c+3] == piece):
                    return True

        # Check vertical locations for win
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if (self.grid[r][c] == piece and self.grid[r+1][c] == piece and
                    self.grid[r+2][c] == piece and self.grid[r+3][c] == piece):
                    return True

        # Check positively sloped diagonals
        for c in range(self.cols - 3):
            for r in range(self.rows - 3):
                if (self.grid[r][c] == piece and self.grid[r+1][c+1] == piece and
                    self.grid[r+2][c+2] == piece and self.grid[r+3][c+3] == piece):
                    return True

        # Check negatively sloped diagonals
        for c in range(self.cols - 3):
            for r in range(3, self.rows):
                if (self.grid[r][c] == piece and self.grid[r-1][c+1] == piece and
                    self.grid[r-2][c+2] == piece and self.grid[r-3][c+3] == piece):
                    return True

        return False
    
    def is_full(self):
        return all(cell != 'O' for cell in self.grid[0])
    
    def get_result(self):
        if self.has_winner('R'):
            return -1
        elif self.has_winner('Y'):
            return 1
        elif self.is_full():
            return 0
        return None
    
    def switch_player(self):
        self.player = 'Y' if self.player == 'R' else 'R'
    
    def copy(self):
        return Board([row[:] for row in self.grid], self.player)
    