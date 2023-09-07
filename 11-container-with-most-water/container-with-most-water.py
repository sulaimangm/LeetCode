class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        volume = 0
        while start < end:
            volume = max(min(height[start], height[end]) * (end-start), volume)
            if(height[start] < height[end]):
                start += 1
            else:
                end -= 1
        return volume