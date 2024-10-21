def qubesum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i ** 3
    return sum
print(qubesum(4, 5))