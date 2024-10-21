def targetsum(arr, target):
    for i in range(len(arr)):
        cursum = 0
        for j in range(i, len(arr)):
            cursum += arr[j]
            if cursum == target:
                print(arr[i:j+1])

arr = [1, 2, 3, 4, 5]
target = 7
targetsum(arr, target)