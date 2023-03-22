import re

inp = input("Please type in anything: ")
pattern = re.compile(r"(?=.[!@#$%^&*?.])")
search = pattern.search(inp)

for letter in inp:
    if letter.isdigit():
        if int(inp) % 2 == 0:
            print(f"This is an even digit:  {letter}")
        else:
            print(f"This is an odd digit:  {letter}")
    elif letter.isupper():
        print(f"This is an uppercase character:  {letter}")
    elif letter.islower():
        print(f"This is an lowercase character:  {letter}")
    elif search:
        print(f"This is a special character:  {letter}")
