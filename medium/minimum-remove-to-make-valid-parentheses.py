# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0 # extra closing parenthesis
        for c in s:
            if c == '(':
                count += 1
                res.append('(')
            elif c == ')' and count > 0:
                res.append(')')
                count -= 1
            elif c != ')': 
                res.append(c)
            
        filtered = []
        for c in res[::-1]:
            if c == '(' and count > 0:
                count -= 1
            else:
                filtered.append(c)
        return ''.join(filtered[::-1])
        

        return res
        
