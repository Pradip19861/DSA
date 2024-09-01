def twosum(nums, target):
    seen = {}
    
    for i in range (len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
print(twosum([2, 3, 4], 5))