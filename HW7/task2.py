def fibonacci(n):
    if n in [1,2]:
        return 1
    if n in [0]:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Please type in a number: "))
terms = {"n": n, "xn": fibonacci(n)}
print(terms)
fibonacci(n)