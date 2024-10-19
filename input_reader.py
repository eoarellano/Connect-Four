def read_input(filename: str):
    with open(filename) as f:
        algorithm = f.readline().strip()
        player = f.readline().strip()
        grid = [list(f.readline().strip()) for _ in range(6)]
    return algorithm, player, grid
