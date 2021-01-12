def recursive_DFS(v, discovered = []):
    discorver.append(v)
    for i in graph[v]:
        if i not in discovered:
            discovered = recursive_DFS(i, discovered)

    return discovered

def iterative_DFS(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.appenc(v)

            for w in graph[v]:
                stack.append(w)

    return discovered

