import random
from search_algorithms import bfs
from visualization import visualize


class Maze:
    def __init__(self, rows: int, cols: int, end: tuple[int, int]):
        self.grid = []
        self.rows = rows
        self.cols = cols
        self.end = end

    def generate_maze(self) -> list[list[int]]:
        self.grid = [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]
        return self.grid

    def print_maze(self):
        for row in self.grid:
            print(row)

    def solve_maze(self):
        path = bfs(self.grid, self.end)
        return path

    def visualize_path(self, path):
        visualize(self.grid, path)


if __name__ == "__main__":
    maze = Maze(5, 5, (4, 4))
    maze.generate_maze()
    maze.print_maze()