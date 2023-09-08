class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        unique =[]
        nums.sort()
        for i in range(len(nums)):
            first = i+1
            last = len(nums)-1
            while first < last:
                if i == first or i == last or first == last:
                    break
                if nums[i] + nums[first] +nums[last] == 0:
                    output.append([nums[i] , nums[first] , nums[last]])
                    first += 1
                    last -= 1
                elif nums[i] + nums[first] +nums[last] > 0:
                    last -= 1
                else:
                    first += 1
        [unique.append(x) for x in output if x not in unique]
        return unique


        