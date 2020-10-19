number = 0
sum = 0

while number < 1000:
    number = number + 1
    if number % 3 != 0:
        continue
    sum = sum + number

print(sum)