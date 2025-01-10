class Solution(object):
    def isPalindrome(self, x):
            x=str(x)
            if x == x[::-1]:
                return True
            else:
                return False
    
# Example usage:
x = 121
solution = Solution()
print(solution.isPalindrome(x))  # Output: True