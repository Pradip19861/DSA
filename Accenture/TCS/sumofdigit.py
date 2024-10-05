def sumofdigit(n):
    count = 0
    while n > 0:
        s = n % 10  # Get the last digit
        count += s  # Add it to the sum
        n = n // 10  # Remove the last digit
    if count % 3 == 0:
        return True
    else:
        return False

print(sumofdigit(132))
