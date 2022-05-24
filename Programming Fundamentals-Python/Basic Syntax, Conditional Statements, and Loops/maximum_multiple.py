divisor = int(input())
boundary = int(input())
max_multiplier = 0
for number in range(boundary , divisor, -1):
    if number % divisor == 0:
        max_multiplier = number
        break

print(max_multiplier)
