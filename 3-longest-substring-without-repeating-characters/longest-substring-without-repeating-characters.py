class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        window = []
        for r in range(len(s)):
            window.append(s[r])
            while window.count(s[r]) > 1:
                l += 1
                window.pop(0)
            length = max(length, len(window))
        return length
                

            