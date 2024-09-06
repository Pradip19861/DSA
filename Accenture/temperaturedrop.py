def temperaturedrop(arr):
    count = 0
    max_count = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            count += 1
        else:
            max_count = max(max_count,count)
            count = 0
    max_count = max(max_count,count)
    return max_count
n = list(map(int,input().split()))
print(temperaturedrop(n))