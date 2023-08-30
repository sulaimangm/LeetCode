class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for index, char in enumerate(s):
            if index == len(s) - 1:
                output += roman[char]
            else:
                if roman[s[index]] < roman[s[index+1]]:
                    output -= roman[char]
                else:        
                    output += roman[char]
        return output

            