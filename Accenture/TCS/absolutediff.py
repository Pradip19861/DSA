def absdiff(n,k):
    ans = 0
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if abs(n[i] - n[j]) == k:
                ans += 1
    return ans
print(absdiff([1,2,2,1], 1))