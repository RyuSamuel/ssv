import heapq
from typing import List
A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
B = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
heap = []

for i in B:
    heapq.heapify(B)

print(B)



def maxHeapify(A: List[int], i: int):

    i = i - 1 #starts from 0
    left = (i * 2) + 1

    if len(A) > left:
        right = (i * 2) + 2

        if A[left] <= len(A) and A[left] > A[i]:
            largest = left

        else:
            largest = i

        if A[right] <= len(A) and A[right] > A[largest]:
            largest = right

        if not largest == i:
            A[i], A[largest] = A[largest], A[i]
            maxHeapify(A, (largest + 1))

    return A

print(maxHeapify(A, 1))
print(maxHeapify(A, 3))

def minHeapify(A: List[int], i: int):

    smallest = i
    left = (i * 2) + 1
    right = (i * 2) + 2

    if left <= len(A) and A[left] < A[smallest]:
        smallest = left

    if right <= len(A) and A[right] < A[smallest]:
        smallest = right

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest)

    return A


print(minHeapify(A, 1))
print(minHeapify(A, 3))