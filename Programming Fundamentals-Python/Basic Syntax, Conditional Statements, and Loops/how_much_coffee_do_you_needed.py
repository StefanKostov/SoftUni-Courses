
command = ""
coffee = 0
while command.lower() != "end":
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" or \
            command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            coffee += 1
        else:
            coffee += 2

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
