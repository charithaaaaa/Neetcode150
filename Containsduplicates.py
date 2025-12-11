class Solution:
    def hasDuplicate(self, nums):
        new_nums = set(nums)
        if len(nums) != len(new_nums):
            return True
        else:
            return False
# Example usage:
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4, 5]))