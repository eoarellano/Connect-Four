import sys
import random
from board import Board
from monte_carlo import monte_carlo_search
from input_reader import read_input
from uct_algorithm import uct_search

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 connect_four.py <input_file> <verbose_mode> <simulations>")
        return

    input_file = sys.argv[1]
    verbose = sys.argv[2] == "Verbose"
    simulations = int(sys.argv[3])
    
    algorithm, player, grid = read_input(input_file)
    board = Board(grid, player)
    
    if algorithm == "PMCGS":
        monte_carlo_search(board, simulations, verbose)
    elif algorithm == "UR":
        move = random.choice(board.get_valid_moves())
        print(f"FINAL Move selected: {move + 1}")
    elif algorithm == "UCT":
        uct_search(board, simulations, verbose)
    else:
        print(f"Unknown algorithm: {algorithm}")

if __name__ == "__main__":
    main()
