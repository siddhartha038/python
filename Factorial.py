

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial cannot be found for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    print("Factorial of", num, "is", factorial(num))
