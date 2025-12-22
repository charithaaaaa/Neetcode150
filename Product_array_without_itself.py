class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
# Example usage:
sol = Solution()
nums = [1, 2, 3, 4]
print("Input:", nums)
output = sol.productExceptSelf(nums)
print("Output:", output)  # Output should be [24, 12, 8, 6]
