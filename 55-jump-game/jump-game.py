class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        currentIndex = 0
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= lastIndex:
                lastIndex = i
        return not lastIndex            
