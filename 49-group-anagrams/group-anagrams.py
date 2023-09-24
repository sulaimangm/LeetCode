class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        sorted_strs = []
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(i)
            else:
                anagrams[sorted_str] = [i]
        return list(anagrams.values())
