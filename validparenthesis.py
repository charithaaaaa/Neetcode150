class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #To store open brackets
        mapping={")":"(","]":"[","}":"{"} # to match closed to open 
        for ch in s:
            if ch in mapping:  #closed brackets
                 if not stack or stack.pop()!=mapping[ch]:
                    return False
            else:
                stack.append(ch) #append open brackts
        return not stack



# Example usage:
s = "()[]{}"
solution = Solution()
print(solution.isValid(s))  # Output: True