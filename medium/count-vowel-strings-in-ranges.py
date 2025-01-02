# https://leetcode.com/problems/count-vowel-strings-in-ranges/


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        count = 0
        res = {0: count}
        for i, s in enumerate(words): 
            if s[0] in vowels and s[-1] in vowels:
                count += 1
            res[i+1]= count
        return [
            res[q[1]+1] - res[q[0]]
            for q in queries
        ]


            



        
