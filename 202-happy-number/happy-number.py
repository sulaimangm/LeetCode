class Solution:
    def isHappy(self, n: int) -> bool:
        duplicates = []
        while n != 1:
            sums = 0
            digits = list(map(int, str(n)))
            if digits in duplicates:
                return False
            else:
                duplicates.append(digits)
            for i in digits:
                sums += i * i
            n = sums
        return True