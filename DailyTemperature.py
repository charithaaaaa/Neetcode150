class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        result=[0]*n
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                result[prev]=i-prev
            else:
                stack.append(i)
        return result
# Example usage:
# temperatures = [73,74,75,71,69,72,76,73
# sol = Solution()
# print(sol.dailyTemperatures(temperatures))  # Output: [1, 1