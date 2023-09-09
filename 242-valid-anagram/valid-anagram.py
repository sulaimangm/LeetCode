class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t);
        # if len(s) != len(t):
        #     return False;
        # for i in range(len(s)):
        #     if (s[i] != t[i]):
        #         return False;
        # return True;
        # Doing character counter is auguably better
        if len(s) != len(t):
            return False
        s_counts = {}
        t_counts = {};
        for i in s:
            s_counts[i] = s_counts.get(i, 0) + 1
        for i in t:
            t_counts[i] = t_counts.get(i, 0) + 1

        if s_counts == t_counts:
            return True
        return False