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
            print(curr.getData())
            curr = curr.getNextNode()

myList = LinkedList()
myList.addNode(5)
myList.addNode(7)
myList.addNode(8)
myList.addNode(9)


def oddEven(head: Node):

    odd = head
    even = head.nextNode
    even_head = head.nextNode

    while even and even_head:
        odd.nextNode = odd.nextNode.nextNode
        odd = odd.nextNode
        even.nextNode = even.nextNode.nextNode
        even = even.nextNode


    odd.nextNode = even_head
    return head

