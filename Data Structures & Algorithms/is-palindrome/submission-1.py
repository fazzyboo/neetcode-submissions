class Solution:
    def isPalindrome(self, s: str) -> bool:
        nestr = ''
        for c in s:
            if c.isalnum():
                nestr += c.lower()
        
        return nestr == nestr[::-1]