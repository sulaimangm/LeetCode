class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        window = {}
        for r in range(len(s)):
            if s[r] in window and window[s[r]] >= l:
                l = window[s[r]] + 1
            window[s[r]] = r
            length = max(length, r-l+1)
        return length
                

            