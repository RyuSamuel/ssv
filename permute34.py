from typing import List
import itertools


def permute(input:List[int]):

    result = []
    prev_elements = []

    def DFS(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            DFS(next_elements)
            prev_elements.pop()

    DFS(input)
    return result


case = [1,2,3]

print(permute(case))

def permutePythonicWay(input:List[int]):
    return list(map(list, itertools.permutations(input)))

print(permutePythonicWay(case))