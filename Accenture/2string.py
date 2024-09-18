def twostring(m,n):
    res = ""
    for i in range(len(m)):
        for j in range(len(n)):
            if m[i] == n[j]:
                res += m[i]
    return res
m = input()
n= input()
print(twostring(m,n))