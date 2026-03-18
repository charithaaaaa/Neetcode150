class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = nums[0]
        
        start = 0
        end = 0
        temp_start = 0
        
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
                temp_start = i   # potential new start
            
            curr_sum += nums[i]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = temp_start
                end = i
        
        return nums[start:end+1]