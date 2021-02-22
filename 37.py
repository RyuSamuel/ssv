from typing import List

def subsets(nums: List[int]):
    result = []

    def DFS(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            DFS(i + 1, path + [nums[i]])

    DFS(0,[])

    return result


print(subsets([1,2,3]))
