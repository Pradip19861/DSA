def middleelement(nums):
    res = []
    for i in range (len(nums)-1):
        if nums[i] >= 0:
            res.append(nums[i])
            mid = res[len(res)//2]
    return mid
print(middleelement([1,-2,3,-4,5,6,7]))