def isValid(s: str) -> bool:
    stack = []

    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'

            if mapping[char] != top_element:
                return False

        else:
            stack.append(char)

    return not stack '''return not을 쓰면 true false를 물음'''

test = "()"

print(isValid(test))