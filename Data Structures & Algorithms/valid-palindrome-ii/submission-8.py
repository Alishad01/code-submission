class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
            
        i, j = 0, len(s)-1
        while i < j :
            if s[i] != s[j]:
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
            i, j = i+1, j-1
            