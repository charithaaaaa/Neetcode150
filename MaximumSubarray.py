class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            global_sum = max(global_sum, current_sum)
        return global_sum

# Example usage:
# nums = [-2,1,-3,4,-1,2,1,-5 ,4]
# solution = Solution()
# print(solution.maxSubArray(nums))  # Output: 6