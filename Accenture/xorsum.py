def sum_xor(n,a):
    sum = 0
    xor = 0
    for i in range(n):
        if i % 2 == 0:
            xor ^= a[i]
        else:
            sum += a[i]
    return sum - xor

A = int(input())
B = list(map(int,input().split()))
result = sum_xor(A,B)
print(result)