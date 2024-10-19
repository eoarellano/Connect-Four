class Node:
    def __init__(self, move=None):
        self.move = move
        self.wins = 0
        self.visits = 0
        self.children = {}
        self.parent = None  
