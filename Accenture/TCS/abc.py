def total_coins(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

# Example usage:
n = int(input())  # Take input for number of days
print(total_coins(n))
