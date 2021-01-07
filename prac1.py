def add_it_up(num: int):
    output = 0

    if isinstance(num, int) != True:
        return 0

    for i in range(num):
        output += i

    output += num
    return output

print(add_it_up(7))

import string

def caesar(s: string, shift: int):
    letters = string.ascii_lowercase
    mask = letters[shift:] + letters[:shift]
    trans = str.maketrans(letters, mask)

    return s.translate(trans)

print(caesar("Hello", 5))

a=[1,2,3,4,5]
b=[2,3,4]
c=[4,5]

print(list(zip(a,b)))