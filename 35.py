def combine(n : int, num: int):
    result = []

    def DFS(element: int, start: int, num: int):
        if num == 0:
            result.append(element[:])

        for i in range(start, n + 1):
            element.append(i)
            DFS(element, i + 1, num - 1)
            element.pop()

    DFS([], 1, num)

    return result


print(combine(4,2))