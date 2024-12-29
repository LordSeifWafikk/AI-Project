# TODO: implement search algorithms

from collections import deque

def bfs(grid, end):
    start = (0, 0)  # Starting point at (0, 0)
    
    # Ensure start and end are valid
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None  # No path if start or end is blocked
    
    queue = deque([start])
    visited = set()
    parent = {start: None}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while queue:
        current_node = queue.popleft()

        if current_node == end:
            # Reconstruct the path from start to end
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Return reversed path

        visited.add(current_node)
        x, y = current_node

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                parent[(nx, ny)] = current_node

    return None  # Return None if no path is found

def dfs(grid, end):
    start = (0, 0)  # Starting point at (0, 0)
    
    # Ensure start and end are valid
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None  # No path if start or end is blocked
    
    stack = [start]
    visited = set()
    parent = {start: None}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while stack:
        current_node = stack.pop()

        if current_node == end:
            # Reconstruct the path from start to end
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Return reversed path

        if current_node not in visited:
            visited.add(current_node)
            x, y = current_node

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    parent[(nx, ny)] = current_node

    return None  # Return None if no path is found
