while True:
    a = input("Write some text please: ")
    if a.isalpha():
        print(f"All characters in your text are alphabets and the message is {len(a)} characters long")
    elif a.isdigit():
        print("All characters in your text are digits")
        if (int(a) % 2) == 0:
            print("Your number is even")
        else:
            print("Your number is odd")
    else:
        print("You used both characters and digits in your text")
