def is_subset(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    return set2.issubset(set1)

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [2, 7, 4]
print(is_subset(array1, array2))  # Output: True
