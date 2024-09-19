def candybuy(n,a,m):
    res = 0
    for i in range(len(a)):
        if a[i] <= m:
            res += 1
            m -= a[i]
        if a[i] % 5 == 0:
            res += 1
    return res
print(candybuy(3,[1,3,2,5],5))