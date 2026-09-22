class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        changes = 1    
        i, j = 0, len(s)-1
        while i < j :
            if changes != 0:
                if s[i] != s[j]:
                    changes-=1
                    return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
            else:
                return False
            i, j = i+1, j-1
        return True
