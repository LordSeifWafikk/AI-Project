import sys

import pygame

from search_algorithms import bfs, dfs
from visualization import SearchVisualizer

if __name__ == "__main__":
    # Add options in GUI to change the maze
    visualizer = SearchVisualizer()
    visualizer.screen.fill((0, 0, 0))
    visualizer.draw_grid()
    pygame.display.update()
    pygame.time.delay(1000)
    # Add options in GUI to change the search algorithm
    visualizer.run_search(bfs)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
