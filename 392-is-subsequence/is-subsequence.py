class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        sPointer = 0
        for i in t:
            if sPointer < len(s):
                if i == s[sPointer]:
                    sPointer += 1
        print(sPointer)
        if sPointer == len(s):
            return True
        return False