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
    
    def has_winner(self):
        # check horizontal win
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (self.grid[row][col] != 'O' and
                    all(self.grid[row][col] == self.grid[row][col + i] for i in range(4))):
                    return self.grid[row][col]
        
        # checks vertical win
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if (self.grid[row][col] != 'O' and
                    all(self.grid[row][col] == self.grid[row + i][col] for i in range(4))):
                    return self.grid[row][col]
        
        # check diagonal
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (self.grid[row][col] != 'O' and
                    all(self.grid[row + i][col + i] == self.grid[row][col] for i in range(4))):
                    return self.grid[row][col]
                
                if (self.grid[row + 3][col] != 'O' and
                    all(self.grid[row + 3 - i][col + i] == self.grid[row + 3][col] for i in range(4))):
                    return self.grid[row + 3][col]
        
        return None
    
    def is_full(self):
        return all(cell != 'O' for cell in self.grid[0])
    
    def get_result(self):
        winner = self.has_winner()
        if winner == 'R':
            return -1
        elif winner == 'Y':
            return 1
        elif self.is_full():
            return 0
        return None
    
    def switch_player(self):
        self.player = 'Y' if self.player == 'R' else 'R'
    
    def copy(self):
        return Board([row[:] for row in self.grid], self.player)
