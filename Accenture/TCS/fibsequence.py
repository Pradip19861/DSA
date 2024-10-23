def fibseqsum(n):
    r, l = 0,1
    if n == 0:
        return r
    if n == 1:
        return l
    fibsum  = 1
    for i in range(2,n):
        cur = r + l
        fibsum += cur
        r , l = l , cur
    return fibsum
n = int(input())
print(fibseqsum(n))