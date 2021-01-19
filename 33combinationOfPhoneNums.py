from typing import List

def commbinationPhoneNums(digits: str) -> List[str]:

    def dfs(index, path): #탐색 시작 -> 끝까지 다하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)): #입력한 자릿수 단위 반복
            for j in dic[digits[i]]: #숫자에 해당되는 모든 문자열을 반복
                dfs(i + 1, path + j)  

    if not digits:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "nmo", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    dfs(0, "")

    return result


print(commbinationPhoneNums("234"))
