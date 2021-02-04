"""def BFS(start_v):

    discovered = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)

        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered
"""
from typing import List

def numIslands(grid: List[List[str]]):
    def DFS(i, j):
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid) or \
            grid[i][j] != '1':
            return

        grid[i][j] = 0

        DFS(i + 1, j)
        DFS(i - 1, j)
        DFS(i, j + 1)
        DFS(i, j - 1)

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                DFS(i, j)
                count += 1

    return count

print(numIslands('111001111'))