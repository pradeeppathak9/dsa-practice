# https://leetcode.com/problems/word-subsets/

from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        min_char_count = defaultdict(int)
        for w in words2:
            char_count = defaultdict(int)
            for c in w:
                char_count[c] += 1
                min_char_count[c] = max(char_count[c], min_char_count[c])
        
        ans = []
        for w in words1:
            char_count = defaultdict(int)
            for c in w:
                char_count[c] += 1
            
            is_universal = True
            for c, count in min_char_count.items():
                if count > char_count[c]:
                    is_universal = False
                    break
            
            if is_universal:
                ans.append(w)
            
        return ans


            

        

         

        
