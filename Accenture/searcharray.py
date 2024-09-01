def searching(nums,target):
    for i in range (len(nums)-1):
        if nums[i] == target:
            return i
        i += 1
print(searching([1,2,3,4],3))