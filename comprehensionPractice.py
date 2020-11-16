#1.List Comprehention
#
# [출력표현식 for 요소 in 입력Sequence [if 조건식]]

from typing import List
import collections
"""
arr = [1,-1,3,-5,8]

def pracOne(arr:List[int]):
    newArr = []
    for i in range(len(arr)):
        if arr[i] < 0:
            newArr.append(arr[i])

    return newArr

print(pracOne(arr))
"""
"""
n = [17,18,5,4,6,1]

def greatestElement(n:List[int]):

    arr = []
    l = len(n)

    for i in range(l-1):
        newArr = max(n[i+1:])
        arr.append(newArr)

    arr.append(-1)

    return arr

print(greatestElement(n))
"""
"""
start_prompt = ['1', '2', '5']

def pracOne(arr:List[int]):
    dict = {'1': 'Test', '2': 'Assignments', '5': 'Homeworks'}
    subject = [dict[i] for i in start_prompt if i in dict]
    return subject

print(pracOne(start_prompt))

#2.Set Comprehention
#
#{출력표현식 for 요소 in 입력Sequence [if 조건식]}
"""
"""

def getSmall(n:int):
    numbers = range(1, n + 1)
    sumSquare = sum(i ** 2 for i in numbers)
    squareSum = sum(numbers)**2

    result = squareSum - sumSquare
    return result

print(getSmall(100))

"""
"""
def isPrime(n:int):
    rangeOfPrime = range(2, int(n**0.5)+1)

    for i in rangeOfPrime:
        if n % i == 0:
            return False
    return True

def primeChecker(index):
    n = 2
    n_prime = 1

    while n_prime < index:
        n = n + 1
        if isPrime(n) == True:
            n_prime = n_prime + 1

    return n

print(primeChecker(10001))
"""
"""
def isPalindrome(s:str):
    stringList = []

    for i in s:
        if i.isalnum():
            stringList.append(i.lower())

    while len(stringList) > 1:
        if stringList.pop(0) != stringList.pop():
            return False

    return True

print(isPalindrome("hello"))
"""
"""
def reverseString(s:str):
    return s[::-1]

print(reverseString("hello"))
"""
"""
def reverseStringMK2(s:List[str]):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

print(reverseStringMK2("hello"))
"""
"""
logs = ["dig1 8 1 5", "let1 art can", "let2 own kit dig", "dig2 3 6", "let3 art zero"]

def reorderLogfiles(logs: List[str]):

    digits = []
    letters = []

    for i in logs:
        if i.split()[1].isdigit():
            digits.append(i)

        else:
            letters.append(i)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits

print(reorderLogfiles(logs))
"""
"""
import collections
import re


def mostCommonWord(string:str, banned:List[str]):
    words = [i for i in re.sub(r'[^\w]', ' ', string).lower().split()
             if i not in banned]


    counts = collections.defaultdict(int)
        for i in words:
            counts[i] += 1

    return max(counts, key=counts.get)

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
"""
"""
a = [1,2,3,6,5,3,2]
print(sorted(a))

b = 'sdg2es'
print(sorted(b))

print("".join(sorted(b)))

c = ['asd','w34td','asdsg','1235']
print(sorted(c,key=len))
print(c.sort())#sort는 리턴값이 없음. 따라서 None으로 출력이됨

d = ['abc', 'cde', 'cfd']

def fn(s):
    return s[0], s[-1]

print(sorted(c, key = fn))

print(sorted(d, key = lambda ab: (ab[0], ab[-1])))
"""
"""
s = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagram(s:List[str]):
    anagram = collections.defaultdict(list)

    for i in s:
        anagram[''.join(sorted(i))].append(i) #'원하는 기준'.join( 바꾸고싶은 문자열 또는변수 )

    return sorted(anagram.values(), key= lambda x : len(x), reverse = True)

print(groupAnagram(s))
"""
"""
string = "123454321"

def longestPalindrome(s:str):
    def expand(left:int, right: int):
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += right

        return s[left - 1: right - 1]

    if len(s) <= 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2))

    return result


print(longestPalindrome(string))

"""
"""
import time
import datetime
start = time.time()

n = [2,7,11,15]

def targetNum(n:List[int], target: int):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == target:
                return [i,j]

sec = time.time() - start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)

print(targetNum(n, 18))
"""

nums = [2,7,11,15]
"""
def targetNumMK2(nums:List[int], target: int):

    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

print(targetNumMK2(nums, 26))
"""
"""
def twoSum(nums: List[int], target: int):

    nums_map = {}

    for i, n in enumerate(nums):
        nums_map[n] = i

    for i, n in enumerate(nums):
        if target - n in nums_map and i != nums_map[target - n]:
            return nums.index(n), nums_map[target - n]

print(twoSum(nums, 18))
"""
"""
n = [0,1442,1245,245,1321,0,125,53,21245,1123,2,1]

def trapping(height:List[int]):
    #높이가 없으면 0으로 출력
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    
    #현재 왼쪽과 오른쪽의 포인터 지점에서 가장 높은 높이를 선언
    left_max, right_max = height[left], height[right]

    #포인터들이 서로 만날때까지 최장높이를 갱신
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        #포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1

        else:
            volume += right_max - height[right]
            right -= 1

    return volume

print(trapping(n))
"""
"""
a = [-1, 0, 1, 2, -1, -4]
def SumThree(arr = List[int]) -> List[List[int]]:

    results = []
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, len(arr) - 1):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

                for k in range(j + 1, len(arr)):
                    if k > j + 1 and arr[k] == arr[k - 1]:
                        continue

                    if arr[i] + arr[j] + arr[k] == 0:
                        results.append((arr[i], arr[j], arr[k]))

    return results

print(SumThree(a))
"""
"""
def sumOfThree(arr:List[int]):
    result = []
    arr.sort()

    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue #배열의 i번째 요소와 이전 요소가 중복될 경우 건너뛰기

        left, right = i + 1, len(arr) - 1

        while left < right:
            sum = arr[i] + arr[left] + arr[right]

            if sum < 0:
                left += 1

            elif sum > 0:
                right -= 1

            else:
                result.append((arr[i], arr[left], arr[right]))

                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                right -= 1
                left += 1

    return result

print(sumOfThree(a))
"""

"""
def test1(arr:List[int]):
    result = []
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1

        while left < right:

            sum = arr[i] + arr[left] + arr[right]

            if sum < 0:
                left += 1

            elif sum > 0:
                right -= 1

            else:
                result.append((arr[i], arr[left], arr[right]))

                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

print(test1(a))
"""
"""
array = [1,4,3,2,5,6]
def arryPart(arr:List[int]):
    sum = 0
    arr.sort()
    pair = []

    for i in arr:
        pair.append(i)

        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


print(arryPart(array))

def arryPart2(arr:List[int]):
    sum = 0
    arr.sort()

    for i, n in enumerate(arr):
        if i % 2 == 0:
            sum += n

    return sum

print(arryPart2(array))

def arryPart3(arr):
    return sum(sorted(arr)[::2])

print(arryPart3(array))
"""
"""
arr = [1,2,3,4]

def arrayTimes(arr:List[int]):
    times = 1
    output = []

    for i in range(0, len(arr)):
        output.append(times)
        times = times * arr[i]

    times = 1

    for i in range(len(arr) - 1, 0 - 1, -1):
        output[i] = output[i] * times
        times = times * arr[i]

    return output

print(arrayTimes(arr))
"""
"""
stocks = [7,1,5,3,6,4]

def stock(arr:List[int]):
    maxP = 0

    for i, price in enumerate(arr):
        for j in range(i, len(arr)):
            maxP = max(arr[j] - price, maxP)

    return maxP

print(stock(stocks))

import sys

def stock2(arr:List[int]):

    profit = 0
    min_price = sys.maxsize #정수의 최댓값을 의미

    for i in arr:
        min_price = min(min_price, i)
        profit = max(profit, i - min_price) #Kadene's algorithm

    return profit

print(stock2(stocks))
"""
"""
arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAna(arr:List[str]):

    anagrams = collections.defaultdict(list)

    for i in arr:
        anagrams[''.join(sorted(i))].append(i)

    return anagrams.values()

print(*groupAna(arr))
"""
"""
arr = [1,2,0,-1,-4,-1]

def addThree(arr:List[int]):
    result = []
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = len(arr) - 1

        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < 0:
                left += 1

            elif sum > 0:
                right -= 1

            else:
                result.append((arr[i], arr[left], arr[right]))

                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

print(addThree(arr))
"""


arr = [1,2,3,2,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
def isPalindrome(head:ListNode):
    q: List = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

print(isPalindrome(arr))
"""
import collections
"""
def isPalindromeDeque(head:ListNode):
    q: Deque = collections.deque()

    if not head:
        return True

    node = head


    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

print(isPalindromeDeque(arr))

"""
"""
def isPalindromeTwo(head:ListNode):

    rev = None
    slow = fast = head

    while fast and fast.next: #while fast and fast.next is not empty, do the followings (or fast and fast.next is true)
        fast = fast.next.next #fast runs in 2 steps
        rev, rev.next, slow = slow, rev, slow.next #store opposite linked list into rev

    if fast: #if number of inputs is odd, slow will move one step in order to exclude the median
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(1)

print(isPalindromeTwo(l))
"""
"""
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print(Solution.mergeTwoLists(l1,l2))
"""

lists = ListNode(1)
lists.next = ListNode(2)
lists.next.next = ListNode(3)
lists.next.next.next = ListNode(4)
"""
class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        if head.next is None:
            return head

        nextNode = head.next
        temp = nextNode.next
        nextNode.next = head #nextNode가 head를 가르키게 되니까 1->2에서 2->1이 됨

        head.next = self.swapPairs(temp)

        return nextNode

print(swapPairs(lists))
"""

def reverseList(self, head: ListNode) -> ListNode:
    def reverse(node, prev: ListNode = None):
        if node is None:
            return prev

        next, node.next = node.next, prev

        return reverse(next, node)

    return reverse(head)

print(reverseList(lists))