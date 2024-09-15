def divtwooreven(a):
    sum = 0
    for i in range(len(a)):
        if a[i] % 2 == 0 or a[i] % 3 == 0:
            sum += a[i]
    return sum

print(divtwooreven([1,2,3,4,5,6,7,8]))