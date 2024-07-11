
def is_prime(num):
    # If the number is less than 2, it's not prime
    if num < 2:
        return False
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
