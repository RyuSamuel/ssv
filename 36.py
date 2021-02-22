from typing import List

def candidates(cands: List[int], tar = int):

    result = []

    def DFS(sum, index, path):
        if sum < 0:
            return

        if sum == 0:
            result.append(path)
            return

        