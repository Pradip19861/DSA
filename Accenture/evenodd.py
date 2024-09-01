def seperateevenodd(nums):
    a = []
    b = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            a.append(nums[i])
        else:
            b.append(nums[i])
        c = a + b
    return c
print(seperateevenodd([1,2,3,4,5,6,7,8,9]))