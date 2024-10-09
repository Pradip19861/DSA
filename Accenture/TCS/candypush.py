def push_empty_packets_to_end(arr):
    # Count the number of zeros in the array
    zero_count = arr.count(0)
    
    # Remove all zeros from the array
    arr = [i for i in arr if i != 0]
    
    # Add the zeros to the end of the array
    arr.extend([0] * zero_count)
    
    return arr

# Input
arr = list(map(int, input().split()))  # Take input as a list of integers

# Function call
result = push_empty_packets_to_end(arr)

# Print result
print(result)
