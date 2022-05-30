n = int(input())
balanced = 0
for i in range(n):
    string = input()
    if string == "(":
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
    elif string == ")":
        balanced -= 1
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")

number_of_lines = int(input())
closed = 0
opened = 0
for i in range(number_of_lines):
    command = input()
    if command == "(":
        closed += 1
        if closed > 1:
            print("UNBALANCED")
            exit()
    elif command == ")":
        opened += 1
if closed == opened:
    print("BALANCED")
else:
    print("UNBALANCED")






