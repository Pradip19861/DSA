def candyproblem(n, arr, M):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 5 == 0:
            count += 1
        else:
            if arr[i]<= M:
                count +=1 
                M -= arr[i]
    return count
print(candyproblem(3,[5,15,3,3],4))