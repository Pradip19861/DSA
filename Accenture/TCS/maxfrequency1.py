def maxfrequency(arr):
    arr.sort()
    max = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == arr[i + 1]:
            count += 1
            if count > max:
                max = count
        i += 1