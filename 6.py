import types
from typing import List
import collections

class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


myList = LinkedList()
myList2 = LinkedList()

myList.addNode(5)
myList.addNode(7)
myList.addNode(8)

myList2.addNode(3)
myList2.addNode(6)
myList2.addNode(2)


class Solution:
    def reverseLists(self, head:Node):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def convertNodeListToList(self, node:Node)->List:

        arr: List = []

        while node:
            arr.append(node.val)
            node = node.next

        return arr


    def convertListToNodeList(self, resultNode:Node):

        prev: Node = None
        for i in resultNode:
            node = Node(i)
            node.next = prev
            prev = node

        return node

    def addLists(self, arr1:List[int], arr2:List[int])->List[int]:
        
        a = self.convertNodeListToList(self.reverseLists(arr1))
        b = self.convertNodeListToList(self.reverseLists(arr2))

        result = int(''.join(str(e) for e in a)) + \
                 int(''.join(str(e) for e in b))

        return self.convertListToNodeList(str(result))

print(Solution.addLists(myList,myList2))