import collections
import heapq
from typing import List

def kFrequent(nums:List[int], k: int):

    freq = collections.Counter(nums)
    freq_heap = []

    for f in freq:
        heapq.heappush(freq_heap, (-freq[f], f))

    topK = list()

    for _ in range(k):
        topK.append(heapq.heappop(freq_heap)[1])

    return topK

sample = [1,1,2,2,2,3]

print(kFrequent(sample, 2))