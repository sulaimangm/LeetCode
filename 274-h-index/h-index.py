class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        length = len(citations)
        if length == 1 and citations[0] > 0:
            return 1
        if citations[-1] >= length:
            return length
        for i in range(length):
            if citations[i] < i+1:
                return i
        return 0
