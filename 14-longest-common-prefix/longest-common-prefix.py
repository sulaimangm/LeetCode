class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        counter = 0
        for i in range(len(strs[0])):
            for j in strs:
                if j[i] != strs[0][i]:
                    break
                counter += 1
            if(counter % len(strs) != 0):
                break
        return strs[0][0:counter//len(strs)]

