from typing import List
import itertools


def permute(input:List[int]):

    result = []
    prev_elements = []

    def DFS(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:] #[:] 리스트의 모든걸 복사. 다만 참조가 되지 않도록 값 자체를 복사하는 방식(ID가 다름)
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

89113114407