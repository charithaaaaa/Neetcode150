class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # Stop early if current number > 0
            if nums[i] > 0:
                break

            # Skip duplicate values for i # present 1 value mundu 1 value same vundadu
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
