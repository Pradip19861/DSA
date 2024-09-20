def cookies(greed, size):
    count = 0
    greed.sort()
    size.sort()
    
    i = 0  # Pointer for greed
    j = 0  # Pointer for size

    while i < len(greed) and j < len(size):
        if greed[i] <= size[j]:
            count += 1
            i += 1  # Move to the next child
        j += 1  # Move to the next cookie regardless

    return count

print(cookies([1, 2], [1, 2, 3]))  # Output: 2