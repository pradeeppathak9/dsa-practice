# https://leetcode.com/problems/palindromic-substrings/

def solution(s): 
    ans = 0
    for i in range(len(s)):
        # check for palindrome of odd length
        j = k = i
        while True:
            if j < 0 or k == len(s) or s[j] != s[k]:
                break
            ans += 1
            j -= 1
            k += 1
        
        # check for palindrome of even length
        j, k = i, i+1
        while True:
            if j < 0 or k == len(s) or s[j] != s[k]:
                break
            ans += 1
            j -= 1
            k += 1
    return ans


class Solution:
    def countSubstrings(self, s: str) -> int:
        return solution(s)
        
