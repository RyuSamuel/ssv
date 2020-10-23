#a = ['Life', 'is', 'too', 'short']
#b = " ".join(a)
#print(b)

"""
a = (1, 2, 3)
b = (4,)
a = a+ b
print(a)
"""
""""
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = set(a)
print(a)
"""
"""
x = 1
while x <= 5:
    print("*" * x)
    x = x + 1
"""
"""
for x in range(0,99):
    print(x)
"""
"""
myList = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for x in myList:
    total += x

avg = total / len(myList)
print(avg)
"""
"""
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
"""
"""
def is_odd(number):
    #number = input("Enter the integer to check whether it's odd:")
    if number % 2 == 1:
        print("The number is odd number.")
    else:
        print("The number is even number.")

is_odd(3)
"""
"""
def my_average(*args):
    result = 0
    for i in args:
        result = result + i

    return result / len(args)

print(my_average(1,2))
print(my_average(3,4,61,25,6123))
"""
"""
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = (int(input1)) +  (int(input2))
print("두 수의 합은 %s 입니다" % total)
"""
"""
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(11)
cal.minus(7)

print(cal.value)
"""
"""
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value <= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력
"""
"""
array = [1, 2, abs(-3)-3]
print(all(array))
"""
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        key = 0
        mySet = dict()

        for x in nums:
            if x:
                mySet[key] = count + 1
                count = count + 1
            else:
                count = 0
                key = key + 1

        if len(mySet) > 0:
            return sorted(mySet.values(), reverse=True)[0]

        else:
            return 0
"""
"""
def isPalindrome(s: str):
    strings = []

    for x in s:
        if s.isalnum():
            strings.append(x.lower())

    return strings

print(isPalindrome("A man, a plan, a canal: Panama"))
"""
"""
def mult_of_three_five(i = int):
    n = i
    result = 0
    while n > 0:
        for n in range(1, 1000):
            if n % 3 == 0 or n % 5 == 0:
                result += n

    return result


a = mult_of_three_five(1000)

print(a)

"""
"""
class testCase:
    def __init__(self):
        pass

    def evenFibo(i : int):
        a, b = 1, 1
        result = 0

        while a <= i:
            if a % 2 == 0:
                result += a
        a, b = b, a + b
        return result

doIt = testCase()
doIt.evenFibo(40)

"""

"""
i = 2
n = 600851475143

while i * i <= n:
    if n % i:
        i += 1

    else:
        n //= i

print(n)
"""
"""
def findingAllFactors(n: int):
    i = 2
    facList = []

    while i * i <= n:
        if n % i:
            i += 1

        else:
            n //= i
            facList.append(i)

    if n > i:
        facList.append(n)

    return facList

print(findingAllFactors())


"""
"""
a = [1, 2, 3, 3, 4, 5, 5, 6]

print(list(enumerate(a)))

for i, v in enumerate(a):
    print(i,v)

for i in range(len(a)):
    print(i, a[i])
"""
"""
def two_sum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

"""
"""

result = 0


for n in range (1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print(result)

"""
"""
print(sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))

"""
"""
def reverse(x: int):

    sign = 1
    if x >= 2**31-1 or x <= -2**31:
        return "Error!"

    while int(x):
        if x % 10 == "0":
            x = x / 10
        else:
            break

    sign = -1 if x < 0 else 1
    x = sign * x

    x = str(x)
    lst = list(x)
    lst.reverse()
    x = "".join(lst)
    x = int(x)

    return sign * x

print(reverse(-1231241244535))
"""
"""
from typing import List

arr = [1, 0, 2, 3, 0, 4, 5, 0]

def duplicateZeros(arr: List[int]):
    arrB = [0 for s in range(len(arr))]
    i = 0

    for i in arr:
        if arr[i] != 0:
            arrB[i] = arr[i]

        else:
            arrB[i] = arr[i]
            arrB[i] = arr[i + 1]

    return arrB

print(duplicateZeros(arr))
"""
"""
from typing import List

A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
result = []

def mergeSort(A: List[int], size_A: int, B: List[int], size_B: int):
    if len(A) < size_A + size_B:
        print("The size of array A is less than the total input!")

    if len(A) >= size_A + size_B:
        result = A + B
        result.sort()

        for i in result:
            if result[i] == 0:
                result.remove(i)

    return result

print(mergeSort(A, m, B, n))
"""
"""
from typing import List

nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums: List[int], val: int) -> int:

    count = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


print(removeElement(nums, val))
"""
"""for i in nums:
       if nums[i] == val:
           nums.remove(i)

   return len(nums)"""
"""
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    count = 0

    for i in range(1,len(nums)):
        if nums[i] != nums[i - 1]:
            nums[count] = nums[i]
            count += 1

    return count

nums = [0,0,1,1,1,2,2,3,3,4]


print(removeDuplicates(nums))


"""
from typing import List
"""
arr = [3,1,7,11]
arr.sort()
for i in range(1, len(arr)):
    if 2 * arr[i] == arr[i + 1]:
        print("True")
"""
"""
def checkIfExist(arr: List[int]) -> bool:
    arr.sort()
    for i in range(0, len(arr)):
        if 2 * arr[i] == arr[i + 1]:
            return True

        elif 2 * arr[i] != arr[i + 1]:
            i = i + 1

    return False

print(checkIfExist(arr))"""
"""
arr = [3,6,7,11]

def checkIfExist(arr: List[int]) -> bool:
    coveredSet = set()
    for n in arr:
        if n * 2 in coveredSet or n / 2 in arr:
            return True
        else:
            coveredSet.add(n)
    return False

print(checkIfExist(arr))
"""
"""
arr = [1,2,2,1]

def mArray(arr:List[int]):
    N = len(arr)
    i = 0
    #Climbing up
    while i < N - 1 and arr[i] < arr[i + 1]:
        i = i + 1
    #If peak is the first or the last, return false
    if i == 0 or i == N - 1:
        return False
    #if peak is redundant, return false, for the peak must be exist as the only one.
    if i + 1 == (len(arr) / 2) and arr[i] == arr[i + 1]:
        return False

    #Climbing down
    while i < N - 1 and arr[i] > arr[i + 1]:
        i = i + 1

    return True

print(mArray(arr))
"""
"""
arr = [1,2,3,4,2,1]

def twoSquare(arr:List[int]):
    result = arr

    if result is None:
        return None

    for i in range(0, len(arr)):
        if (i - 1) % 2 == 0:
            arr[i] *= arr[i]

    result[i] = arr[i]

    return result

print(twoSquare(arr))


def twoSquareV2(arr:List[int]):
    if arr is None:
        return None

    for i in range(0, len(arr)):
        if i % 2 != 0:
            arr[i] = arr[i] * arr[i]

    return arr

print(twoSquareV2(arr))
"""
"""
arr = [1,2,3,4,2,1]
def replaceElements(arr:List[int])-> List[int]:
    result = []

    for i in range(len(arr) - 1):
        comp = max(arr[i+1:])
        result.append(comp)

    result.append(-1)

    return result

print(replaceElements(arr))
"""
"""
arr = [1,2,3,4,2,1]
def listSum(arr:List[int]):
    if len(arr) == 1:
        return arr[0]

    else:
        return arr[0] + listSum(arr[1:])

print(listSum(arr))
"""

def recurSum(x:int):
    if x == 1:
        return x

    return x + recurSum(x - 1)

print(recurSum(4))

def factorialRecur(x:int):
    if x == 1:
        return 1

    return x * factorialRecur(x - 1)

print(factorialRecur(4))

def MultofthreeFive(x:int)->int:
    temp = []

[출력표현식 for 요소 in 입력Sequence [if 조건식]]