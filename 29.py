import collections

def numJewelsInStones(J: str, S: str):

    freq = {}
    counter = 0

    #돌의 빈도 수 합산
    for char in S:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    #보석의 빈도 수 합산
    for char in J:
        if char in freq:
            counter += freq[char]

    return counter

print(numJewelsInStones("aA", "aAAbbbb"))

def numJewelsInStonesTwo(J: str, S: str):
    freq = collections.defaultdict(int)
    counter = 0

    for char in S:
        freq[char] += 1

    for char in J:
        counter += freq[char]

    return counter

print(numJewelsInStonesTwo("aA", "aAAbbbb"))

def numJewlsInStonesThree(J: str, S: str):
    freq = collections.Counter(S)
    counter = 0

    for char in J:
        counter += freq[char]

    return counter

print(numJewlsInStonesThree("aA", "aAAbbbb"))

#def numJewelsInStonesFour(J, S):



















def stonesAndJewels(S: str, J: str):
    freq = {}
    count = 0

    for char in S:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    for char in J:
        if char in freq:
            count += freq[char]

    return count

print(stonesAndJewels("aAbB","aAAbbbb"))


def stonesAndJewels2(S, J):

    freq = collections.defaultdict(int)
    count = 0

    for char in S:
        freq[char] += 1

    for char in J:
        count += freq[char]

    return count

print(stonesAndJewels2("aA", "aAAbbbb"))

def stonesAndJewels3(S, J):

    freq = collections.Counter(S)
    count = 0

    for char in J:
        count += freq[char]

    return count

print(stonesAndJewels3("aA", "aAAbbbb"))