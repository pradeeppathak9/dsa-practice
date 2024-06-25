# https://leetcode.com/problems/valid-palindrome/

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_set =set(string.ascii_lowercase + string.digits)
        s = [ c.lower() for c in s if c.lower() in valid_set]
        i, j = 0, len(s) - 1
        while j > i:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
