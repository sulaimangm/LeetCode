class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i in range(len(nums)):
            if nums[i] in indices:
                a = indices[nums[i]][-1]
                if i - a <= k:
                    return True
                indices[nums[i]]. append(i)
            else:
                indices[nums[i]] = [i]