def buycandy(arr, m):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 5 == 0:
            count += 1
        else:
            if arr[i] <= m:
                count += 1
                m -= arr[i]
    return count

arr = list(map(int, input().split()))

m = int(input())

print(buycandy(arr, m))
