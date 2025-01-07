# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        res = set()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]: 
                    res.add(words[i])
                if words[j] in words[i]: 
                    res.add(words[j])
        return list(res)
            
                    
                




        
