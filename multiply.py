# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Input the numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Multiply the numbers
result = multiply(num1, num2)

# Display the result
print("The product of {} and {} is {}".format(num1, num2, result))
