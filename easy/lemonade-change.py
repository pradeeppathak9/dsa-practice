# https://leetcode.com/problems/lemonade-change/

from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_collected = defaultdict(int)
        for b in bills:
            bills_collected[b] += 1
            change_required = b - 5
            while change_required > 0: 
                transacted= False
                for b in [20, 10, 5]:
                    if bills_collected[b] > 0 and change_required >= b:
                        change_required -= b
                        bills_collected[b] -= 1
                        transacted = True
                        
                if not transacted: 
                    return False
        return True





    
                



        
