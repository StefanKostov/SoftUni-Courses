budget = int(input())
flag = False
while True:
    sum = input()
    if sum == "End":
        print("You bought everything needed.")
        flag = True
        break
    budget -= int(sum)
    if budget < 0:
        print("You went in overdraft!")
        break
