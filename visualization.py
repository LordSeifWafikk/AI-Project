import pygame

from maze_generation import Maze


class SearchVisualizer:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze Solver")
        self.grid_size = 50
        self.maze = Maze(5, 5, (4, 4))
        self.width, self.height = 250, 250
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.grid = self.maze.generate_maze()
        self.maze.print_maze()

    def draw_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == 0:
                    color = (255, 255, 255)
                elif self.grid[y][x] == 1:
                    color = (255, 0, 0)
                elif self.grid[y][x] == 2:
                    color = (0, 255, 0)

                pygame.draw.rect(self.screen, color,
                                 (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))

    def run_search(self, algorithm: callable):
        path = self.maze.solve_maze(algorithm)
        for step in path:
            x, y = step
            self.grid[y][x] = 2
            self.draw_grid()
            pygame.display.update()
            pygame.time.delay(500)
