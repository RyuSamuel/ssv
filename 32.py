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


def MinHeapify(A, i):
    i = i - 1

    if i == 0:
        left = 1
        right = 2
    else:
        left = (i * 2) + 1

    if len(A) > (i * 2) + 1:  # If a node has left children
        if A[left] <= len(A) and A[left] < A[i]:
            smallest = left
        else:
            smallest = i

        if len(A) > (i * 2) + 2:  # If a node has a right child
            right = (i * 2) + 2

            if A[right] <= len(A) and A[right] < A[smallest]:
                smallest = right

        if not smallest == i:
            A[i], A[smallest] = A[smallest], A[i]
            MinHeapify(A, (smallest + 1))  # Because i = i-1

    return A


def minHeapify(A: List[int], i: int):

    i = i - 1

    if i == 0:
        left = 1
        right = 2
    else:
        left = (i * 2) + 1

    if len(A) > (i * 2) + 1:
        if A[left] <= len(A) and A[left] < A[i]:
            smallest = left
        else:
            smallest = i

        if len(A) > (i * 2) + 2:
            right = (i * 2) + 2

            if A[right] <= len(A) and A[right] < A[smallest]:
                smallest = right

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            minHeapify(A, (smallest + 1))

    return A

print(MinHeapify(A, 1))
print(MinHeapify(A, 3))
print(minHeapify(A, 1))
print(minHeapify(A, 3))