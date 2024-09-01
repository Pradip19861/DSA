def fibnocciseries(n):
    if n == 1 or n == 0:
        return n
    f = 0
    l = 1
    for i in range(2,n+1):
        curr = f+l
        f = l 
        l = curr
    return l
print(fibnocciseries(4))