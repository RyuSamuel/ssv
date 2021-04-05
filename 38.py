from typing import List
import collections
#import igraph


def recursive_DFS(graph, v, discovered):
    discovered.append(v)

    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_DFS(graph, w, discovered)

    return discovered

graph_list = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

discovered = []

print(recursive_DFS(graph_list, 1, discovered))