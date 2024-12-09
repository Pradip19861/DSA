def swap_numbers(a, b):
    # Swap using addition and subtraction
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage
print(swap_numbers(5,10))  # Output: x = 10, y = 5
