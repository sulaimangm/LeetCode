class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1[m-1])
        for i in range(n):
            nums1[m+i] = nums2[i]
        print(nums1.sort())