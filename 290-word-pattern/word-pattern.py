class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        matches = {}
        s = s.split()
        words = {}
        
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in matches:
                if matches[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in words:
                    return False
                matches[pattern[i]] = s[i]
                words[s[i]] = pattern[i]
        return True   
