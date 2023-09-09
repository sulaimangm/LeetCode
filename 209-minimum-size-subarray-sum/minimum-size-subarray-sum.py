class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subarrayLength = []
        l = 0
        result = 0
        length = float('inf')
        for r in range(len(nums)):
            result += nums[r]
            while result >= target:
                length = min(length, r-l+1)
                result -= nums[l]
                l += 1
        return 0 if length == float('inf') else length