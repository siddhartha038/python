
def series_sum(n):
    sum = 0
    sign = 1  # To alternate between addition and subtraction
    
    for i in range(1, n+1):
        # Calculate the numerator and denominator
        numerator = 2*i - 1
        denominator = 2*i
        
        # Calculate the term and add/subtract it to the sum
        term = sign * (numerator / denominator)
        sum += term
        
        # Alternate the sign for the next term
        sign *= -1
    
    return sum

# Input the number of terms from the user
n = int(input("Enter the number of terms: "))

# Call the function and print the result
result = series_sum(n)
print("The summation of the series is:", result)
