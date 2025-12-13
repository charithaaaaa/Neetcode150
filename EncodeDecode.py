from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # find the delimiter '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length

        return res

# Example usage:
sol = Solution()
encoded_str = sol.encode(["hello", "world"])
print("Encoded:", encoded_str)
decoded_list = sol.decode(encoded_str)
print("Decoded:", decoded_list)
