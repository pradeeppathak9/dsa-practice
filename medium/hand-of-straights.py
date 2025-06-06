# https://leetcode.com/problems/hand-of-straights/

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        counts = Counter(hand)
        keys = sorted(counts.keys())
        j = 0
        while j < len(keys):
            if counts[keys[j]] > 0:
                start = keys[j]
                for i in range(groupSize):
                    if counts[start + i]:
                        counts[start + i] -= 1
                    else:
                        return False
            else:
                j += 1
        return True




      
      
