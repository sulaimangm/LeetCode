class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        matches = []

        for i in range(len(s)):
            if s[i] in letters:
                if letters[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] not in matches:
                    letters[s[i]] = t[i]
                    matches.append(t[i])
                else:
                    return False 
        return True