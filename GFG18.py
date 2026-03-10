class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)

        count = 0

        for i in range(n):
            count += next_smaller[i] - i

        return count