def contiguoussubarr(arr,k):
    ans = []
    for i in range(len(arr) - k+1):
        maxi = arr[i]
        for j in range(i, i+k):
            maxi = max(maxi,arr[j])
        ans.append(maxi)
    print(*ans)
arr = list(map(int,input().split()))
k = int(input())
contiguoussubarr(arr, k)