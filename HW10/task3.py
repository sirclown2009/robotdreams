import re

emails = []
print("To quit enter 'q'")
filename_input = input("Enter file name: ")
while True:
    email_input = input("Enter your email: ")
    if email_input == "q":
        break
    emails.append(email_input)
    email_sub = re.sub(r"(?<=.)[a-z][^@]\w+(?=.)", "***", email_input)
    # i tried to figure out how to hide everything except for the first and last letters,
    # but only managed to hide the first one
    # could you please help me with that?
    if email_sub:
        print(email_sub)

with open(filename_input, "w") as f:
    for item in emails:
        f.write("%s\n" % item)
