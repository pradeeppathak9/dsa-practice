# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = set(spaces)
        for i, s in enumerate(s):
            if i in spaces:
                res += ' '
            res += s
        return ''.join(res)


        
