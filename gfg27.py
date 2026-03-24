from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        # Build graph
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        # Queue for nodes with 0 indegree
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == n
# example
# n = 2, prerequisites = [[1,0]]
# Output: True  