class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = i+1
            last = len(nums)-1
            while first < last:
                sums = nums[i] + nums[first] +nums[last]
                if sums == 0:
                    output.append([nums[i] , nums[first] , nums[last]])
                    while first < last and nums[first] == nums[first + 1]:
                        first += 1
                    while first < last and nums[last] == nums[last - 1]:
                        last -= 1
                    first += 1
                    last -= 1
                elif sums > 0:
                    last -= 1
                else:
                    first += 1
        return output


        