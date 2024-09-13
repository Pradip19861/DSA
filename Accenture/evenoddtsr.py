def evenoddstr(n,a):
    res = ""
    for i in range(n):
        if a[i] % 2 == 0:
            res += "even"
        else:
            res += "odd"
    return res

n = int(input())

a = list(map(int, input().split()))

print(evenoddstr(n, a))