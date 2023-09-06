class Solution:
    def isPalindrome(self, s: str) -> bool:
        aplhanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower() 
        s = ''.join([char for char in s if char in aplhanumeric])
        if s[::-1] == s:
            return True
        return False