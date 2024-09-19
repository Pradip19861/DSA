def difference(n, m):
    res1 = 0  # To store sum of multiples of 'n'
    res2 = 0  # To store sum of non-multiples of 'n'
    
    for i in range(1, m+1):  # Loop from 1 to m
        if i % n == 0:
            res1 += i  # Add to res1 if multiple of 'n'
        else:
            res2 += i  # Add to res2 if not a multiple of 'n'
    
    return res2 - res1  # Return the difference

print(difference(4, 20))  # Expected output
