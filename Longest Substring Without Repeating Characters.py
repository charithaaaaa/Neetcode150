class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        hash_set=[]
        n=len(s)
        i=0
        for j in range(0,n):
            while s[j]in hash_set:
                hash_set.remove(s[i])
                i+=1
            hash_set.append(s[j])
            max_len=max(max_len,j-i+1)
        return max_len
        
        