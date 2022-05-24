number_of_strings = int(input())
for command in range(number_of_strings):
    command = input()

    if "," in command or "." in command or "_" in command:
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")