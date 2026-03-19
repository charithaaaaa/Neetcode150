class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
#         No need to copy the remaining elements of nums1, as they are already in place.
#example
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6] 