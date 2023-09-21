class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            n = 0
            temp = i
            while nums2[n] != temp:
                n += 1
            for j in range(n, len(nums2)):
                if nums2[j] > temp:
                    temp = nums2[j]
                    output.append(temp)
                    break
            if temp == i:
                output.append(-1) 
        return output