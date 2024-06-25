# https://leetcode.com/problems/longest-palindromic-substring/

def solution(s): 
    max_length = 0
    res = ''
    for i in range(len(s)):
        # check for palindrome of odd length
        j = k = i
        while True:
            if j < 0 or k == len(s) or s[j] != s[k]:
                break
            if k - j + 1 > max_length:
                max_length = k-j+1
                res = s[j: k+1]
            j -= 1
            k += 1
        
        # check for palindrome of even length
        j, k = i, i+1
        while True:
            if j < 0 or k == len(s) or s[j] != s[k]:
                break
            if k - j + 1 > max_length:
                max_length = k-j+1
                res = s[j: k+1]
            j -= 1
            k += 1
    return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return solution(s)
        
