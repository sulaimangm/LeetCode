class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        for i in t:
            if sPointer < len(s):
                if i == s[sPointer]:
                    sPointer += 1
            else:
                break
        if sPointer == len(s):
            return True
        return False