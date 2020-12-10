import collections
from typing import List

class CircularQueue:

    def __init__(self, q:int):
        self.q = [None] * q
        self.maxLen = q
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxLen
            return True

        else:
            return False

    def deQueue(self):
        if self.p1 is None:
            return True
        else:
            self.q[self.p2] = None
            self.p1 = (self.p1 + 1) % self.maxLen
            return True

    def front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None

