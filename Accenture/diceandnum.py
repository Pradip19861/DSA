def dicesum(n,a):
    sum = 0
    if n % 2 == 0:
        for i in range(len(a)):
            if i % 2 != 0:
                sum += a[i]
    else:
        for i in range(len(a)):
            if i % 2 == 0:
                sum += a[i]
    return sum
print(dicesum(2,[1,2,3,4]))