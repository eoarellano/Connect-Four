import random
from board import Board
from node import Node

def monte_carlo_search(board: Board, simulations: int, verbose: bool):
    root = Node()
    initial_player = board.player

    for i in range(simulations):
        current = root
        node_path = []
        last_move = (-1, -1)

        while True:
            result = board.get_result(last_move)
            if result is not None:
                break

            valid_moves = board.get_valid_moves()
            if not valid_moves:
                break

            unexplored = [m for m in valid_moves if m not in current.children]
            
            if current != root and verbose:
                print(f"wi: {current.wins}")
                print(f"ni: {current.visits}")
                print(f"Move selected: {current.move}")

            if unexplored:
                move = random.choice(unexplored)
                new_node = Node(move)
                new_node.parent = current
                current.children[move] = new_node
                last_move = board.make_move(move)
                if verbose:
                    print("NODE ADDED")
                node_path.append((new_node, last_move))
                break
            
            move = random.choice(list(current.children.keys()))
            last_move = board.make_move(move)
            current = current.children[move]
            node_path.append((current, last_move))
            board.switch_player()

        # SIMULATION (Rollout)
        sim_last_move = last_move
        while board.get_result(sim_last_move) is None:
            moves = board.get_valid_moves()
            move = random.choice(moves) if moves else None
            if move is not None:
                sim_last_move = board.make_move(move)
                board.switch_player()

        result = board.get_result(sim_last_move)
        if verbose:
            print(f"TERMINAL NODE VALUE: {result}")

        # BACKPROPAGATION
        if verbose:
            print("Updated values:")
        for node, move in reversed(node_path):
            node.visits += 1
            if (result == 1 and initial_player == 'Y') or (result == -1 and initial_player == 'R'):
                node.wins += 1
            if verbose:
                print(f"wi: {node.wins}")
                print(f"ni: {node.visits}")
            board.undo_move(move)
            board.switch_player()

    # Select the best move
    moves_values = {}
    for col in range(7):
        if col in root.children:
            node = root.children[col]
            value = node.wins / node.visits if node.visits > 0 else 0
            if verbose:
                print(f"Column {col + 1}: {value:.2f}")
            moves_values[col] = value
        else:
            if verbose:
                print(f"Column {col + 1}: Null")
            moves_values[col] = float('-inf')

    best_move = max(moves_values.items(), key=lambda x: x[1])[0]
    if verbose:
        print(f"\nFINAL Move selected: {best_move + 1}")
    return best_move