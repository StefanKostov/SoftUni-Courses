current_year = int(input())
while True:
    current_year += 1
    year = str(current_year)
    if len(set(year)) == len(year):
        print(year)
        break
