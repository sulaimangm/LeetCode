class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = s.split()
        s = ""
        for i in range(len(words)-1, -1, -1):
            s += words[i]
            if i > 0:
                s += " "
        return s