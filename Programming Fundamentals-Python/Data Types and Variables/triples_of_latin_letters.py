number_of_triples = int(input())
for i in range(number_of_triples):
    for j in range(number_of_triples):
        for k in range(number_of_triples):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
