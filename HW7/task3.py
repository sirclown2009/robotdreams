def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# I wanted to use n == [0, 1]:
#   return 1
# but it didn't work out, could you please explain why?


n = int(input("Please type in a number: "))
d = {"Number: ": n, "Factorial: ": factorial(n)}
print(d)