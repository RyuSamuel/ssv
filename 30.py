import collections
from typing import List

def substring(S: str):

    used = {}
    max_length = start = 0

    for i, char in enumerate(S):
        if char is used and start <= used[char]:
            start = used[char] + 1

        else:
            max_length = max(max_length, i - start + 1)

        used[char] = i

    return max_length
S = "abcabcbb"
print(substring(S))


