class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        counter = 1
        nums.sort()
        for i in range(length-1):
            if nums[i] == nums [i+1]:
                counter += 1
                if counter > length/2:
                    return nums[i]
            else:
                counter = 1
        return nums[length-1]