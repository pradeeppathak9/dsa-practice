# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        ans = []
        def backtrack(res, i):
            if i == len(digits):
                if len(res):
                    ans.append(''.join(res))
                return
            for c in mapping[digits[i]]:
                backtrack( res + [c], i+1)

        backtrack([], 0)
        return ans
