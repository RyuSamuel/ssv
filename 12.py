import collections

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

"""
def removeDups(self, s: str):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]

    if set(s) == set(suffix):
        return char + self.removeDups(suffix.replace(char,''))

    return ''
"""

def removeDups(s:str):
    counters = collections.Counter(s)
    seen = set()
    stack = []

    for char in s:
        counters[char] -= 1
        if char is seen:
            continue

        while stack and char < stack[-1] and counters[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return ''.join(stack)

print(removeDups('adadvsddds'))