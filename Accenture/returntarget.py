n = [int(x) for x in input().split()]
target = int(input())
a=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if (n[i]+n[j]==target):
            a.append((i,j))
print(a)
