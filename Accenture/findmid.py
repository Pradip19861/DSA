def find_positive_mid_element(n, arr):
    # Filter out negative numbers
    positive_numbers = [num for num in arr if num >= 0]
    
    # Find the mid-index
    mid_index = len(positive_numbers) // 2
    
    # Print the element at the mid-index
    print(positive_numbers[mid_index])

# Example usage
n = 6
arr = [12, -14, 36, 77, 13, 14]
find_positive_mid_element(n, arr)
