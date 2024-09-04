def evensum(a):
    sum = 0
    n = len(a)
    for i in range(len(a)):
        rdx = n - i -1
        if rdx % 2 == 0:
            sum += a[i]
    return sum

a = list(map(int, input().split()))
print(evensum(a))
