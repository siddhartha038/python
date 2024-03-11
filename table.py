# Taking input from the user
num = int(input("Enter a number: "))

# Printing the table of the entered number
print("Table of", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
