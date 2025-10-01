class MazeSolver:
    def __init__(self, matrix: list) -> None:
        """
        MazeSolver class to find a valid path in a maze and collect coins.
        Args:
            matrix (list): 2D list representing the maze.
        """
        self.matrix = matrix
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.path, self.coins = [], []
        self._find_path(0, 0)
        self._fix_path()

    def _is_valid_move(self, x: int, y: int) -> bool:
        """
        Check if a move is valid and update the coins list.
        Args:
            x (int): X-coordinate of the move.
            y (int): Y-coordinate of the move.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if 0 <= x < self.rows and 0 <= y < self.cols:
            if self.matrix[x][y] == 2:
                self.coins.append([x, y])
            return self.matrix[x][y] != 1 and [x, y] not in self.path
        return False

    def _find_path(self, x: int, y: int) -> None:
        """
        Recursively find a valid path starting from the given position.
        Args:
            x (int): X-coordinate of the current position.
            y (int): Y-coordinate of the current position.
        Returns:
            None
        """
        if self._is_valid_move(x, y):
            self.path.append([x, y])
            self._find_path(x + 1, y)
            self._find_path(x, y + 1)

    def _fix_path(self) -> None:
        """
        Remove additional positions from the path to end it on the last row.
        Returns:
            None
        """
        self.path = [pos for pos in self.path if pos[0] == self.rows - 1]

# Example usage:
maze_input = [
    [0, 1, 1, 1, 1],
    [0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 2, 0]
]
solver = MazeSolver(maze_input)
print("Valid Path:", solver.path)
print("Collected Coins:", solver.coins)
