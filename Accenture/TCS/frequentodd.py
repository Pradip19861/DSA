from collections import Counter

def smallest_most_frequent_odd():
    # Read the input size (N)
    n = int(input().strip())  # Number of elements in the array
    
    # Read the array elements
    arr = list(map(int, input().strip().split()))
    
    # Filter out only odd numbers from the array
    odd_numbers = [num for num in arr if num % 2 != 0]
    
    # If there are no odd numbers, print -1 and return
    if not odd_numbers:
        print(-1)
        return
    
    # Count the frequency of each odd number
    frequency = Counter(odd_numbers)
    
    # Find the maximum frequency among the odd numbers
    max_frequency = max(frequency.values())
    
    # Collect all odd numbers that have the maximum frequency
    most_frequent_odds = [num for num in frequency if frequency[num] == max_frequency]
    
    # Find the smallest number among the most frequent odd numbers
    result = min(most_frequent_odds)
    
    # Print the result
    print(result)

# Example usage:
# Input:
# 7
# 1 1 1 2 3 3 3
# Expected Output:
# 1
smallest_most_frequent_odd()
