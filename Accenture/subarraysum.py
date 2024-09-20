def maxSubArray( nums):
        sum = 0
        max_sum = float('-inf')
        
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
                
        return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))