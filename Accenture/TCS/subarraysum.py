n = int(input())
a = list(map(int,input().split()))

a.sort()
totalsum = 0
for i in range(len(a)):
    totalsum += a[i]
    if a[i] < totalsum - a[i]:
        print(totalsum)
    else:
        totalsum = totalsum - a[i]
    