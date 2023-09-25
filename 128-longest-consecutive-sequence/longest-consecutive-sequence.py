class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxLength = 0
        elements = set(nums)
        for i in elements:
            if i-1 not in elements:
                current = i
                length = 0
                while current in elements:
                    current += 1
                    length +=1
                maxLength = max(maxLength, length)

        return maxLength
