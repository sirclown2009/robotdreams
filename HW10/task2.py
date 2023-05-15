import re

emails = []
print("To quit enter 'q'")
filename_input = input("Enter file name: ")
while True:
    email_input = input("Enter your email: ")
    if email_input == "q":
        break
    emails.append(email_input)
    email_sub = re.sub(r"([a-zA-z0-9]+[\._]?)*[a-zA-z0-9]@[a-zA-z0-9]+\.\w+", "*@*", email_input)
    if email_sub:
        print(email_sub)

with open(filename_input, "w") as f:
    for item in emails:
        f.write("%s\n" % item)

