number_of_commands = int(input())
for i in range(number_of_commands):
    command = int(input())
    if command == 86:
        print("How are you?")
    if command == 88:
        print("Hello")
    if command < 88 and command != 88 and command != 86:
        print("GREAT!")
    if command > 88:
        print("Bye.")
