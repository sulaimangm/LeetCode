class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elements = {}
        for i in nums:
            elements[i] = []
        for i in elements:
            if i-1 in elements:
                continue
            else:
                elements[i] = [i]
                temp = i+1
                while temp in elements:
                    elements[i].append(temp)
                    temp += 1
        return len(max(elements.values(), key = len))
