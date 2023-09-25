class Solution:
    def isHappy(self, n: int) -> bool:
        duplicates = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in duplicates:
                return False
            else:
                duplicates.add(n)
        return True