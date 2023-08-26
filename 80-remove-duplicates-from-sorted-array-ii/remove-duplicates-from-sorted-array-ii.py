class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            return len(nums)
        for i in range(len(nums)-1, 0, -1):
            if(len(nums) < 3):
                return len(nums)
            if nums[i] == nums[i-1]:
                if nums[i-1] == nums[i-2]:
                    nums.pop(i)
        return len(nums)