class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        result=[]
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        # Sort keys by highest frequency
        sorted_keys = sorted(hash_map, key=lambda x: hash_map[x], reverse=True)

        
        return sorted_keys[:k]
# Example usage:
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))