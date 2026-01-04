class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for char in s:
            if char.isalnum():
                n+=char.lower()
        l=0
        r=len(n)-1
        while l<r:
            if n[l]!=n[r]:
                return False
            l+=1
            r-=1
        return True
# Example usage:
s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))  # Output: True