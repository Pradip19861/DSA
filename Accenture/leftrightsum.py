def leftright(n, k):
    sum1 = 0
    sum2 = 0
    for i in range(0, k):
        sum1 += n[i]
    for j in range(k+1, len(n)):
        sum2 += n[j]
    return abs(sum1 - sum2)

print(leftright([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
