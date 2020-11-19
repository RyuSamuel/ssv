import types
from typing import List
import collections
from slist import SList

from node import Node
from linkedList import LinkedList

def nodeSwwap(node):

    cur = node

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return cur

myList = LinkedList()
myList.addNode(5)
myList.addNode(7)
myList.addNode(8)
myList.addNode(9)

myList.printNode()

#print(nodeSwwap(myList))

