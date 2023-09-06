class Solution:
    def isPalindrome(self, s: str) -> bool:
        aplhanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower() 
        s = ''.join([char for char in s if char in aplhanumeric])
        print(s)
        inverse = s[::-1]
        if inverse == s:
            return True
        return False