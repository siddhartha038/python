def print_pattern(rows):
    """
    Function to print a pyramid pattern of numbers.

    Args:
    rows (int): Number of rows in the pyramid.

    Returns:
    None
    """
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        
        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print numbers in descending order
        for k in range(i - 1, 0, -1):
            print(k, end="")
        
        # Move to the next line
        print()

# Example usage:
num_rows = 5
print_pattern(num_rows)
