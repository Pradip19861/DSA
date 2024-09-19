def missingnum(n):
    n.sort()  # Sort the numbers
    for i in range(len(n) - 1):
        if n[i] + 1 != n[i + 1]:
            return n[i] + 1
    return None  # If no number is missing, return None or you can return the next number after the last

n = list(map(int, input().split()))  # Input list of numbers
print(missingnum(n))
