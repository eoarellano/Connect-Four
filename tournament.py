import random
from board import Board
from monte_carlo import monte_carlo_search
from uct_algorithm import uct_search

class URAlgorithm:
    def select_move(self, board: Board):
        return random.choice(board.get_valid_moves())

class PMCGSAlgorithm:
    def __init__(self, simulations: int):
        self.simulations = simulations

    def select_move(self, board: Board):
        return monte_carlo_search(board, self.simulations, verbose=False)

class UCTAlgorithm:
    def __init__(self, simulations: int):
        self.simulations = simulations

    def select_move(self, board: Board):
        return uct_search(board, self.simulations, verbose=False)

def play_game(algorithm1, algorithm2):
    empty_grid = [['O'] * 7 for _ in range(6)]
    board = Board(empty_grid, 'R')
    
    while True:
        if board.player == 'R':
            move = algorithm1.select_move(board)
        else:
            move = algorithm2.select_move(board)
        
        board.make_move(move)
        
        result = board.get_result()
        if result is not None:
            return result
        
        board.switch_player()

def run_tournament(algorithms, num_games=10):
    results = {alg: {alg: 0 for alg in algorithms} for alg in algorithms}
    
    for i, (name1, alg1) in enumerate(algorithms.items()):
        for j, (name2, alg2) in enumerate(algorithms.items()):
            if i != j:
                wins1, wins2 = 0, 0
                for _ in range(num_games):
                    result = play_game(alg1, alg2)
                    if result == -1:
                        wins1 += 1
                    elif result == 1:
                        wins2 += 1
                results[name1][name2] = wins1 / num_games
                results[name2][name1] = wins2 / num_games
    
    return results

def print_results(results):
    print("Algorithm", end="\t")
    for alg in results:
        print(alg, end="\t")
    print()
    for alg1 in results:
        print(alg1, end="\t")
        for alg2 in results[alg1]:
            print(f"{results[alg1][alg2]:.2f}", end="\t")
        print()

if __name__ == '__main__':
    algorithms = {
        "UR": URAlgorithm(),
        "PMCGS(500)": PMCGSAlgorithm(500),
        "PMCGS(10000)": PMCGSAlgorithm(10000),
        "UCT(500)": UCTAlgorithm(500),
        "UCT(10000)": UCTAlgorithm(10000)
    }
    
    results = run_tournament(algorithms)
    print_results(results)