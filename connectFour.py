import time
import sys

def read_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    algorithm = lines[0].strip()
    player = lines[1].strip()
    board = [list(f.readline().strip()) for _ in range(6)]
    return algorithm, player, board

def valid_move(board, column):

    valid_moves = []

    return True


def main():
    input_file = sys.argv[1]
    
    algorithm, player, board = read_file(input_file)

if __name__ == "__main__":
    main()