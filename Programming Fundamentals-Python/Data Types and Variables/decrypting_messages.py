key = int(input())
lines_of_strings = int(input())
new_string = ""
for i in range(lines_of_strings):
    string = input()
    letter = ord(string)
    new_letter = ord(string) + key
    print(chr(new_letter), end="")
