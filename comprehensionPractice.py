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
string = "ab"

def longestPalindrome(s:str):
    def expand(left: int, right: int):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1

        return s[left + 1:right - 1]

    if len(s) <= 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result,
                     expand(1, i + 1),
                     expand(1, i - 1),
                     key = len)

    return result

print(longestPalindrome(string))

