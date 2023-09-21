class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        output = [-1] * len(nums1)

        for i in nums2:
            while stack and i > stack[-1]:
                greater[stack.pop()] = i
            stack.append(i) 
        
        for i, num in enumerate(nums1):
            if num in greater:
                output[i] = greater[num]
        
        return output
