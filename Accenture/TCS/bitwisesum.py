def subarray_bitwise(arr):
    res = set()  # Use a set to avoid duplicate bitwise OR results
    cur = {0}  # Initialize with 0 to handle edge cases

    for num in arr:
        # Compute bitwise OR for all subarrays ending with 'num'
        cur = {x | num for x in cur} | {num}
        res.update(cur)  # Add all results to 'res'
    
    return len(res)

arr = list(map(int, input("Enter array elements: ").split()))
print(subarray_bitwise(arr))
