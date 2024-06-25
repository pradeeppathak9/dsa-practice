# https://leetcode.com/problems/valid-parentheses/

from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
                continue
            if len(stack) == 0 or stack.pop() != brackets_map[c]:
                return False
        if len(stack):
            return False
        return True

            


        
