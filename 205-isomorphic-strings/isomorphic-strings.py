class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        matches = []

        for i in range(len(s)):
            if s[i] in letters:
                if letters[s[i]] != t[i]:
                    return False
            else:
                if t[i] in matches:
                    return False 
                letters[s[i]] = t[i]
                matches.append(t[i])
        return True