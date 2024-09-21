def maxSubArray( nums,k):
        sum = 0
        count = 0
        max_sum = 0
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
            if max_sum % k == 0:
                count += 1
        return count
        

print(maxSubArray([-2,2],2))