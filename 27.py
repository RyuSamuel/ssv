import heapq
import collections
from typing import List
from node import Node

def mergeKLists(lists: List[Node]):

    root = result = Node(None)
    heap = []

    for i in range(len(lists)):
        if list[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        index = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, index, result.next))


    return root.next