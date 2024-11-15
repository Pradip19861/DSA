def subsequence(arr):
    arr.sort()  # Sort the array
    count = 0
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:  # Count only unique elements
            count += 1
    return count

print(subsequence([5, 3, 1, 3, 3]))  # Output: 3, as there are 3 unique elements (1, 3, 5)